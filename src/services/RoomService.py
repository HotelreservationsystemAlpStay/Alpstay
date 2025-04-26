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
        
    @staticmethod
    def _sqlite3row_to_room(row: sqlite3.Row)-> Room:
        return Room(
            room_id = row['room_id'],
            room_no = row['room_number'],
            price_per_night = row['price_per_night']
        )
        
    def get_available_rooms(self, dateStart: date, dateEnd: date, hotels = [], extendedFilter=[[],[]]) -> None:
        query = """
        SELECT * from extended_room
        """
        results = self.db.fetchall(query)
        rooms = []
        for room in results:
            print(self._sqlite3row_to_room(room))
            
rs = RoomService()
rs.get_available_rooms(None, None)