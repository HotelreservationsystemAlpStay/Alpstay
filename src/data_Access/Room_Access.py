import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.Validator import Validator
from models.Room import Room
from models.RoomType import RoomType
from models.Facility import Facility
from data_Access.Base_Access_Controller import Base_Access_Controller
from data_Access.Facility_Access import Facility_Access
from data_Access.RoomType_Access import RoomType_Access
from datetime import date
import sqlite3



class Room_Access:
    def __init__(self):
        self.db = Base_Access_Controller()
        self._SELECT = "SELECT * from extended_room JOIN Booking ON Booking.room_id = extended_room.room_id"
        self._WHERE = "WHERE"
        self._AND = "AND"
        self._WHERE_BOOKINGDATE = "(Booking.check_in_date BETWEEN ? AND ?) OR (Booking.check_out_date BETWEEN ? AND ?) OR (Booking.check_in_date <= ? AND Booking.check_out_date >= ?)"
        self._WHERE_HOTELID = "extended_room.hotel_id in"
        self._WHERE_ROOMTYPE = "extended_room.type_id = ?"


    @staticmethod
    def _get_seasonal_multiplier(season:str):
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

    def _sqlite3row_to_room(self, row: sqlite3.Row, facilities=[], roomType:RoomType=None, season:str=None) -> Room:
        return Room(
            room_id=row["room_id"],
            room_no=row["room_number"],
            price_per_night= self._get_seasonal_multiplier(season)*row["price_per_night"],
            facilities=facilities,
            roomType=roomType
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
    def _intId_to_roomType(row: int) -> RoomType:
        if row is None or row == 0:
            return []
        rs = RoomType_Access()
        return rs.get_roomtype_by_id(row)

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
            query += f" {self._WHERE} {self._WHERE_HOTELID} ({hotel_ids[0]})"
        else:    
            query += f" {self._WHERE} {self._WHERE_HOTELID} {tuple(hotel_ids)}"
        return query, param

    def _add_roomType(self, query:str, param:list, roomType:RoomType):
        if not roomType or not isinstance(roomType, RoomType):
            return query,param
        if "WHERE" in query: query +=f" {self._AND}"
        if "AND" not in query: query +=f" {self._WHERE}"
        query += f" {self._WHERE_ROOMTYPE}"
        param.append(roomType.id)
        return query, param
                    

    def get_rooms(
        self, dateStart: date = None, dateEnd: date = None, hotel_ids: list[int] = None, roomType:RoomType = None
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
        query, providedList = self._add_roomType(query,providedList, roomType)
        print(f"query {query}")
        print(providedList)
        results = self.db.fetchall(
            query, self._get_list_to_tuple(providedList)
        )
        rooms = []
        for room in results:
            rooms.append(
                self._sqlite3row_to_room(
                    row=room,
                    facilities=self._strId_to_facility(room["facilities_list"]),
                    roomType=self._intId_to_roomType(room["type_id:1"]),
                    season=self._get_season(input_date=dateStart)
                )
            )
        return rooms
    



rs = Room_Access()
print("### 1")
tempRooms = rs.get_rooms(date(2025, 6, 1), date(2025, 6, 5))
for room in tempRooms:
    print(room)
    for facility in room.facilities:
        print(facility)
    print(room.roomType)
print("### 2")
tempRooms = rs.get_rooms(date(2025, 6, 1), date(2025, 6, 5), hotel_ids=[2])
for room in tempRooms:
    print(room)
    for facility in room.facilities:
        print(facility)
    print(room.roomType)
print("### 3")
tempRooms = rs.get_rooms(date(2025, 6, 1), date(2025, 6, 5), hotel_ids=[2, 3, 5])
for room in tempRooms:
    print(room)
    for facility in room.facilities:
        print(facility)
    print(room.roomType)
print("### 4")
tempRooms = rs.get_rooms(date(2025, 6, 1), date(2025, 6, 5), hotel_ids=[2, 3, 5], roomType=RoomType(4,"stuff",2))
for room in tempRooms:
    print(room)
    for facility in room.facilities:
        print(facility)
    print(room.roomType)
