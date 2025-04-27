import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from controller.Validator import Validator
from models.Room import Room
from models.RoomType import RoomType
from models.Facility import Facility
from controller.DataBaseController import DataBaseController
from datetime import date
import sqlite3

class RoomService:
    def __init__(self):
        self.db = DataBaseController()
        self._SELECT = "SELECT * from extended_room JOIN Booking ON Booking.room_id = extended_room.room_id"
        self._WHERE_BOOKINGDATE = " WHERE (Booking.check_in_date BETWEEN ? AND ?) OR (Booking.check_out_date BETWEEN ? AND ?) OR (Booking.check_in_date <= ? AND Booking.check_out_date >= ?)"
        self._WHERE_HOTELID = "extended_room.hotel_id in"
        
    @staticmethod
    def _sqlite3row_to_room(row: sqlite3.Row)-> Room:
        return Room(
            room_id = row['room_id'],
            room_no = row['room_number'],
            price_per_night = row['price_per_night']
        )
        
    def get_available_rooms(self, dateStart=None, dateEnd=None, hotels = []) -> list[Room]:
        query = self._SELECT
        if dateStart != None:
            query += self._WHERE_BOOKINGDATE
        if len(hotels) != 1:
            query += f" AND {self._WHERE_HOTELID} {tuple(hotels)}"
        else:
            query += f" AND {self._WHERE_HOTELID} ({hotels[0]})"
        print(query)
        
        results = self.db.fetchall(query, (dateStart, dateEnd,dateStart, dateEnd,dateStart, dateEnd))
        rooms = []
        for room in results:
            rooms.append(self._sqlite3row_to_room(room))
        return rooms
            
rs = RoomService()
print("### 1")
rs.get_available_rooms(date(2025, 6, 1), date(2025, 6, 5))
print("### 2")
rs.get_available_rooms(date(2025, 6, 1), date(2025, 6, 5), hotels=[2])
print("### 3")
rs.get_available_rooms(date(2025, 6, 1), date(2025, 6, 5), hotels=[2,3,5])