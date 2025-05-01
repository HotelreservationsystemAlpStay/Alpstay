import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.Validator import Validator
from models.RoomType import RoomType
from Data_Access.Base_Access_Controller import Base_Access_Controller
from datetime import date
import sqlite3

class RoomTypeService:
    def __init__(self):
        self.db = Base_Access_Controller()
        self.validator = Validator()

    @staticmethod
    def _sqlite3row_to_roomtype(row: sqlite3.Row)->RoomType:
        return RoomType(
            id=row['type_id'],
            description=row['description'],
            maxGuests=row['max_guests']
        )
    
    def get_all_roomtypes(self, hotels=[]):
        query = "SELECT DISTINCT * FROM Room_Type"
        if len(hotels) != 0:
            if len(hotels) == 1:
                tuples = f"({hotels[0]})"
            else:
                tuples = tuple(hotels)
            query += f"""
            JOIN Room on Room.room_id = Room_Type.type_id
            JOIN Hotel on Hotel.hotel_id = Room.hotel_id
            WHERE Hotel.hotel_id in {tuples}
            ORDER BY Room_Type.type_id
            """
        result = self.db.fetchall(query)
        roomTypes = []
        for item in result:
            roomTypes.append(self._sqlite3row_to_roomtype(item))
        return roomTypes

    def get_roomtype_by_id(self, id:int):
        self.validator.checkID(id)
        query = "SELECT * FROM Room_Type WHERE type_id = ?"
        result = self.db.fetchone(query, (f"{id}"))
        return self._sqlite3row_to_roomtype(result)

    def get_roomtype_by_max_guests(self, max_guests:int):
        self.validator.checkInteger(max_guests, "Id")
        query = "SELECT * FROM Room_Type WHERE max_guests = ?"
        result = self.db.fetchone(query, (f"{max_guests}"))
        return self._sqlite3row_to_roomtype(result)
"""
rrr = RoomTypeServie()

print("1: 2 exp")
shee = rrr.get_all_roomtypes([1])
for s in shee:
    print(s)

print("3: 4 exp")
shee = rrr.get_all_roomtypes([1,2,3])
for s in shee:
    print(s)
"""