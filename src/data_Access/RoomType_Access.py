import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.Validator import Validator
from models.RoomType import RoomType
from data_Access.Base_Access_Controller import Base_Access_Controller
from datetime import date
from controller.User_Controller import User_Controller
import sqlite3

class RoomType_Access:
    def __init__(self):
        self.db = Base_Access_Controller()
        self.validator = Validator()
        self.user_controller = User_Controller()
        self._SELECT = "SELECT DISTINCT * FROM Room_Type"

    @staticmethod
    def _sqlite3row_to_roomtype(row: sqlite3.Row)->RoomType:
        return RoomType(
            id=row['type_id'],
            description=row['description'],
            maxGuests=row['max_guests']
        )
    
    def get_all_roomtypes(self, hotels=[]):
        query = self._SELECT
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
        query = f"{self._SELECT} WHERE type_id = ?"
        result = self.db.fetchone(query, (f"{id}"))
        return self._sqlite3row_to_roomtype(result)

    def get_roomtype_by_max_guests(self, max_guests:int):
        self.validator.checkInteger(max_guests, "Id")
        query = f"{self._SELECT} WHERE max_guests = ?"
        result = self.db.fetchone(query, (f"{max_guests}"))
        return self._sqlite3row_to_roomtype(result)
    
    def add_roomtype(self, description, max_guests, user_id, password):
        is_admin = self.user_controller.check_admin(user_id, password)
        if is_admin == False:
            return None
        query = "INSERT INTO Room_Type (description, max_guests) VALUES (?, ?)"
        params = (description, max_guests)
        cursor = self.db.execute(query, params)
        new_id = cursor.lastrowid
        return new_id  

    def modify_roomtype(self, type_id, description, max_guests, user_id, password):
        is_admin = self.user_controller.check_admin(user_id, password)
        if is_admin == False:
            return False  
        query = "UPDATE Room_Type SET description = ?, max_guests = ? WHERE type_id = ?"
        params = (description, max_guests, type_id)
        Try:
            cursor = self.db.execute(query, params)
            return True
        except: 
            return False



       
"""

rrr = RoomType_Access()

print("1: 2 exp")
shee = rrr.get_all_roomtypes([1])
for s in shee:
    print(s)

print("3: 4 exp")
shee = rrr.get_all_roomtypes([])
for s in shee:
    print(s)
"""


