import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.Validator import Validator
from models.Room import Room
from models.RoomType import RoomType
from models.Facility import Facility
from Base_Access_Controller import Base_Access_Controller
from data_Access.Facility_Access import FacilityService
from data_Access.RoomType_Access import RoomType_Access
from datetime import date
import sqlite3


class Room_Access:
    def __init__(self):
        self.db = Base_Access_Controller()
        self._SELECT = "SELECT * from extended_room JOIN Booking ON Booking.room_id = extended_room.room_id"
        self._WHERE_BOOKINGDATE = " WHERE (Booking.check_in_date BETWEEN ? AND ?) OR (Booking.check_out_date BETWEEN ? AND ?) OR (Booking.check_in_date <= ? AND Booking.check_out_date >= ?)"
        self._WHERE_HOTELID = "extended_room.hotel_id in"

    @staticmethod
    def _sqlite3row_to_room(row: sqlite3.Row, facilities=[], roomType=None) -> Room:
        return Room(
            room_id=row["room_id"],
            room_no=row["room_number"],
            price_per_night=row["price_per_night"],
            facilities=facilities,
            roomType=roomType,
        )

    @staticmethod
    def _strId_to_facility(row: str) -> list[Facility]:
        if row is None or row.strip() == "":
            return []
        listOfFacilities = [int(item.strip()) for item in row.split(",")]
        listOfActualFacilities = []
        for item in listOfFacilities:
            fs = FacilityService()
            listOfActualFacilities.append(fs.get_facility_by_id(facility_id=item))
        return listOfActualFacilities

    @staticmethod
    def _intId_to_roomType(row: int) -> RoomType:
        if row is None or row == 0:
            return []
        rs = RoomType_Access()
        return rs.get_roomtype_by_id(row)

    def get_available_rooms(
        self, dateStart: date = None, dateEnd: date = None, hotel_ids: list[int] = None
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
        query = self._SELECT
        if dateStart:
            query += self._WHERE_BOOKINGDATE
            inLoop = True
        if len(hotel_ids) > 1:
            if inLoop: query += f" AND {self._WHERE_HOTELID} {tuple(hotel_ids)}"
            else :query += f" {self._WHERE_HOTELID} {tuple(hotel_ids)}"
        elif len(hotel_ids) == 1:
            if inLoop: query += f" AND {self._WHERE_HOTELID} ({hotel_ids[0]})"
            else: query += f" {self._WHERE_HOTELID} ({hotel_ids[0]})"
        results = self.db.fetchall(
            query, (dateStart, dateEnd, dateStart, dateEnd, dateStart, dateEnd)
        )
        rooms = []
        for room in results:
            rooms.append(
                self._sqlite3row_to_room(
                    room,
                    facilities=self._strId_to_facility(room["facilities_list"]),
                    roomType=self._intId_to_roomType(room["type_id:1"]),
                )
            )
        return rooms


rs = Room_Access()
print("### 1")
tempRooms = rs.get_available_rooms(date(2025, 6, 1), date(2025, 6, 5))
for room in tempRooms:
    print(room)
    for facility in room.facilities:
        print(facility)
    print(room.roomType)
print("### 2")
rs.get_available_rooms(date(2025, 6, 1), date(2025, 6, 5), hotels=[2])
print("### 3")
rs.get_available_rooms(date(2025, 6, 1), date(2025, 6, 5), hotels=[2, 3, 5])
