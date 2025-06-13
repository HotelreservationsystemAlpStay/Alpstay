from utils.Validator import Validator
from utils.Formatting import Format
from models.Room import Room
from models.Room_Type import Room_Type
from models.Facility import Facility
from data_Access.Base_Access_Controller import Base_Access_Controller
from data_Access.Facility_Access import Facility_Access
from data_Access.Room_Type_Access import Room_Type_Access
from datetime import date
import sqlite3



class Room_Access:
    def __init__(self):
        """Initialize Room Access with database controller and SQL query templates."""
        self.db = Base_Access_Controller()
        self._SELECT = "SELECT DISTINCT extended_room.* from extended_room JOIN Booking ON Booking.room_id = extended_room.room_id"
        self._WHERE = "WHERE"
        self._AND = "AND"
        self._WHERE_BOOKINGDATE = """
        Booking.room_id not IN (
	        SELECT extended_room.room_id from extended_room 
            JOIN Booking ON Booking.room_id = extended_room.room_id 
            WHERE ( 
                (Booking.check_in_date BETWEEN ? AND ?) OR 
                (Booking.check_out_date BETWEEN ? AND ?) OR 
                (Booking.check_in_date <= ? AND Booking.check_out_date >= ?) ) )
            """
        self._WHERE_HOTELID = "extended_room.hotel_id in"
        self._WHERE_ROOMTYPE = "extended_room.type_id = ?"


    @staticmethod
    def _get_seasonal_multiplier(season:str):
        """Get price multiplier based on season.
        
        Args:
            season (str): Season type
            
        Returns:
            float: Price multiplier
        """
        pass
        if season == "Summer":
            return 1.5
        return 1
        
    @staticmethod
    def _get_season(input_date:date):
        """returns season type based on starting date, Months April to Septembert are considered sumemr

        Args:
            date (date): input date
            
        Returns:
            month (str): season
        """
        #if if date is in rage of summer  then return summer
        if 4 <= int(input_date.strftime("%m")) <= 9: 
            return "Summer"
        #else return winter
        return "Winter"

    def _sqlite3row_to_room(self, row: sqlite3.Row, facilities=[], room_Type:Room_Type=None) -> Room:
        return Room(
            room_id=row["room_id"],
            room_no=row["room_number"],
            price_per_night= row["price_per_night"],
            facilities=facilities,
            room_Type=room_Type
        )

    @staticmethod
    def _strId_to_facility(row: str) -> list[Facility]:
        if row is None or row.strip() == "":
            return []
        listOfFacilities = [int(item.strip()) for item in row.split(",")]
        listOfActualFacilities = []
        for item in listOfFacilities:
            fs = Facility_Access()
            listOfActualFacilities.append(fs.get_facility_by_id(facility_id=item))
        return listOfActualFacilities

    @staticmethod
    def _intId_to_roomType(row: int) -> Room_Type:
        if row is None or row == 0:
            return []
        rs = Room_Type_Access()
        return rs.get_Room_Type_by_id(row)

    @staticmethod
    def _get_list_to_tuple(providedList:list):
        return tuple(providedList)

    def _add_dates(self, query:str, param:list, dateStart: date = None, dateEnd: date = None):
        """created filter option for provided dates

        Args:
            dateStart (date, optional): starting date of search request. Defaults to None.
            dateEnd (date, optional): end date of search request. Defaults to None.
        """
        if not dateStart:
            return query, param
        dateStart = dateStart.isoformat()
        dateEnd = dateEnd.isoformat()
        if "WHERE" in query: query +=f" {self._AND}"
        if "AND" not in query: query +=f" {self._WHERE}"
        query += f" {self._WHERE_BOOKINGDATE}"
        param.extend([dateStart,dateEnd,dateStart,dateEnd,dateStart,dateEnd])
        return query,param

    def _add_hotel_ids(self, query:str, param: list, hotel_ids: list[int]):
        if not hotel_ids or len(hotel_ids) < 1:
            return query,param
        if "WHERE" in query: query +=f" {self._AND}"
        if "AND" not in query: query +=f" {self._WHERE}"
        if len(hotel_ids) == 1:
            query += f" {self._WHERE_HOTELID} ({hotel_ids[0]})"
        else:    
            query += f" {self._WHERE_HOTELID} {tuple(hotel_ids)}"
        return query, param

    def _add_roomType(self, query:str, param:list, room_Type:Room_Type):
        if not room_Type or not isinstance(room_Type, Room_Type):
            return query,param
        if "WHERE" in query: query +=f" {self._AND}"
        if "AND" not in query: query +=f" {self._WHERE}"
        query += f" {self._WHERE_ROOMTYPE}"
        param.append(room_Type.id)
        return query, param
                   
    def get_room(self, room_id:int):
        query = f"{self._SELECT} WHERE extended_room.room_id = ?"
        room = self.db.fetchone(query=query, params=(room_id,))
        return self._sqlite3row_to_room(
                    row=room,
                    facilities=self._strId_to_facility(room["facilities_list"]),
                    room_Type=self._intId_to_roomType(room["type_id:1"])
                )

    def get_rooms(
        self, dateStart: date = None, dateEnd: date = None, hotel_ids: list[int] = None, room_Type:Room_Type = None
    ) -> list[Room]:
        """returns rooms based on filter

        Args:
            dateStart (date, optional): starting date, if None provided filter for duration will not be applied. Defaults to None.
            dateEnd (date, optional): end date. Defaults to None.
            hotels (list[int], optional): list of hotel id, if None provided filter for hotels will not be applied. Defaults to None.

        Returns:
            list[Room]: rooms filtered on provided args
        """
        providedList = []
        query = self._SELECT
        query, providedList = self._add_dates(query, providedList,dateStart,dateEnd)
        query, providedList = self._add_hotel_ids(query,providedList,hotel_ids)
        query, providedList = self._add_roomType(query,providedList, room_Type)
        results = self.db.fetchall(
            query, self._get_list_to_tuple(providedList)
        )
        rooms = []
        for room in results:
            rooms.append(
                self._sqlite3row_to_room(
                    row=room,
                    facilities=self._strId_to_facility(room["facilities_list"]),
                    room_Type=self._intId_to_roomType(room["type_id:1"])
                )
            )
        return rooms
    
    def get_available_rooms_city(self, city:str, check_in_date: date, check_out_date: date):
        query = """
        SELECT r.room_id, r.room_number, r.price_per_night, h.name AS name, a.city, rt.description AS room_type
        FROM Room r
        JOIN Room_Type rt ON r.type_id = rt.type_id
        JOIN Hotel h ON r.hotel_id = h.hotel_id
        JOIN Address a ON h.address_id = a.address_id
        WHERE a.city = ?
        AND r.room_id NOT IN (
        SELECT b.room_id
        FROM Booking b
        WHERE b.is_cancelled = 0
        AND (
        (b.check_in_date BETWEEN ? AND ?)
        OR (b.check_out_date BETWEEN ? AND ?)
        OR (b.check_in_date <= ? AND b.check_out_date >= ?)))
        """
        #TODO alle check_in und check_out dates abdecken.
        params = (city, check_in_date, check_out_date, check_in_date, check_out_date, check_in_date, check_out_date)
        return self.db.fetchall(query, params)

    def access_available_rooms_hotel_id(self, hotel_id:int, check_in_date: date, check_out_date: date):
        query = """
        SELECT r.room_id, r.room_number, r.price_per_night, rt.description, rt.max_guests, rt.type_id
        FROM Room r
        JOIN Room_Type rt ON r.type_id = rt.type_id
        JOIN Hotel h ON r.hotel_id = h.hotel_id
        JOIN Address a ON h.address_id = a.address_id
        WHERE h.hotel_id = ?
        AND r.room_id NOT IN (
            SELECT b.room_id
            FROM Booking b
            WHERE b.is_cancelled = 0
            AND (
                (b.check_in_date BETWEEN ? AND ?)
                OR (b.check_out_date BETWEEN ? AND ?)
                OR (b.check_in_date <= ? AND b.check_out_date >= ?)
            )
        );
        """
        params = (hotel_id, check_in_date, check_out_date, check_in_date, check_out_date, check_in_date, check_out_date)
        result = self.db.fetchall(query, params)
        rooms = []
        for row in result:
            room = Room(row["room_id"], row["room_number"], row["price_per_night"])
            room_type = Room_Type(row["type_id"], row["description"], row["max_guests"])
            rooms.append((room, room_type))
        return rooms
        
    
    def updateRoom(self, room:Room):
        """Update room information in the database.
        
        Args:
            room (Room): Room object with updated information
            
        Returns:
            Room: Updated room object from database
        """
        query = "UPDATE Room SET room_number = ?, type_id = ?, price_per_night = ? WHERE room_id = ?"
        self.db.execute(query, (room.room_no, room.room_Type.id, room.price_per_night, room.room_id))
        return self.get_room(room.room_id)