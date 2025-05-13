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
        print(str(row))
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

    def _add_dates(self, dateStart: date = None, dateEnd: date = None):
        """created filter option for provided dates

        Args:
            dateStart (date, optional): starting date of search request. Defaults to None.
            dateEnd (date, optional): end date of search request. Defaults to None.
        """
        pass

    def get_available_rooms(
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
        inLoop = False
        providedList = []
        query = self._SELECT
        if dateStart:
            self._add_dates()
            query += f" {self._WHERE} {self._WHERE_BOOKINGDATE}"
            inLoop = True
            providedList.append(dateStart)
            providedList.append(dateEnd)
            providedList.append(dateStart)
            providedList.append(dateEnd)
            providedList.append(dateStart)
            providedList.append(dateEnd)
        if hotel_ids and len(hotel_ids) > 1:
            if inLoop: 
                query += f" AND {self._WHERE_HOTELID} {tuple(hotel_ids)}"
            else:
                inLoop = True
                query += f" {self._WHERE} {self._WHERE_HOTELID} {tuple(hotel_ids)}"
        elif hotel_ids and len(hotel_ids) == 1:
            if inLoop: query += f" AND {self._WHERE_HOTELID} ({hotel_ids[0]})"
            else:
                inLoop = True 
                query += f" {self._WHERE} {self._WHERE_HOTELID} ({hotel_ids[0]})"
        if roomType:
            if inLoop:
                query +=f" {self._WHERE} {self._WHERE_ROOMTYPE}"
            else: 
                inLoop = True
                query +=f" AND {self._WHERE} {self._WHERE_ROOMTYPE}"
            providedList.append(roomType.id)
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
    

"""
    def calculate_room_price_per_stay(self, price_per_night, start_date, end_date):
        query = "SELECT price_per_night FROM room WHERE room_id = ?"
        result = self.db.fetchone(query, (room_id,))

        price_per_night = result[0]

        if isinstance(input_date, str):
            input_date = datetime.strptime(input_date, "%Y-%m-%d").date()

            start_date = (input_date.month, input_date.day)

        spring_season_start = (3-1)
        spring_season_end = (5-31)
        summer_season_start = (6-1)
        summer_season_end = (8-31)
        fall_season_start = (9-1)
        fall_season_end = (11-30)
        winter_season_start = (12-1)
        winter_season_end = (2-28)

        if start_date >= spring_season_start and start_date <= spring_season_end:
            season = "Spring Season"
        elif start_date >= summer_season_start and start_date <= summer_season_end:
            season = "Summer Season"
        elif start_date >= fall_season_start and start_date <= fall_season_end:
            season = "Fall Season"
        elif start_date >= winter_season_start and start_date <= winter_season_end:
            season = "Winter Season"
        elif start_date >= "01-01" and start_date <= "02-28":
            season = "Winter Season"
       
        if season == "Spring Season":
            multiplier = 0.85
        elif season == "Summer Season":
            multiplier = 1.5
        elif season == "Fall Season":
            multiplier = 0.85
        elif season == "Winter Season":
            multiplier = 1.2
        else: multiplier = 1.0

        days = end_date - start_date

        final_price_per_stay = price_per_night * multiplier * days 
        # mit dieser Variante erhällt man für alle Tage die Preise der Saison, in der man begonnen hat mit dem Aufenthalt
        # Es werden so Kunden belohnt, die in der Nebensaison buchen und evtl. auch länger bleiben und Kunden bestraft, die in der Hochsaison buchen
        return final_price_per_stay
    

    # Task Elia: Anzahl Tage einfügen (evtl. Durchschnitt der Preise zusammenrechnen und durch Anzahl Tage teilen, sodass man auch in verscheidenen Saisons einen korrekten Preis erhällt)
    


print("### 2")
rs.get_available_rooms(date(2025, 6, 1), date(2025, 6, 5), hotel_ids=[2])
print("### 3")
rs.get_available_rooms(date(2025, 6, 1), date(2025, 6, 5), hotel_ids=[2, 3, 5])


"""
rs = Room_Access()
print("### 1")
tempRooms = rs.get_available_rooms(date(2025, 6, 1), date(2025, 6, 5))
for room in tempRooms:
    print(room)
    for facility in room.facilities:
        print(facility)
    print(room.roomType)
