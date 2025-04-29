import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from controller.Validator import Validator
from models.RoomType import RoomType
from controller.DataBaseController import DataBaseController
from datetime import date
import sqlite3

class RoomTypeServie:
    def __init__(self):
        self.db = DataBaseController()
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
        params = ()
        if(len(hotels) == 1):
            query += "WHERE "
        result = self.db.fetchall(query, params)
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

rrr = RoomTypeServie()
shee = rrr.get_all_roomtypes()
for s in shee:
    print(s)