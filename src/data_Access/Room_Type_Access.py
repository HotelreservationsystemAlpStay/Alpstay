from utils.Validator import Validator
from models.Room_Type import Room_Type
from data_Access.Base_Access_Controller import Base_Access_Controller
from datetime import date
from managers.User_Manager import User_Manager
import sqlite3

class Room_Type_Access:
    def __init__(self):
        self.db = Base_Access_Controller()
        self.validator = Validator()
        self.user_Manager = User_Manager()
        self._SELECT = "SELECT DISTINCT * FROM Room_Type"

    @staticmethod
    def _sqlite3row_to_Room_Type(row: sqlite3.Row)->Room_Type:
        return Room_Type(
            id=row['type_id'],
            description=row['description'],
            maxGuests=row['max_guests']
        )
    
    def get_all_Room_Types(self, hotels=[]):
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
        Room_Types = []
        for item in result:
            Room_Types.append(self._sqlite3row_to_Room_Type(item))
        return Room_Types

    def get_Room_Type_by_id(self, id:int):
        self.validator.checkID(id)
        query = f"{self._SELECT} WHERE type_id = ?"
        result = self.db.fetchone(query, (f"{id}"))
        return self._sqlite3row_to_Room_Type(result)

    def get_Room_Type_by_max_guests(self, max_guests:int):
        self.validator.checkInteger(max_guests, "Id")
        query = f"{self._SELECT} WHERE max_guests = ?"
        result = self.db.fetchone(query, (f"{max_guests}"))
        return self._sqlite3row_to_Room_Type(result)
    
    def add_Room_Type(self, description, max_guests):
        query = "INSERT INTO Room_Type (description, max_guests) VALUES (?, ?)"
        params = (description, max_guests)
        cursor = self.db.execute(query, params)
        new_id = cursor.lastrowid
        return new_id  

    def modify_Room_Type(self, type_id, description:str=None, max_guests:int=None):
        if not description and not max_guests:
            return False
        elif not description and max_guests:
            query = "UPDATE Room_Type SET max_guests = ? WHERE type_id = ?"
            params = (max_guests, type_id)
        elif description and not max_guests:
            query = "UPDATE Room_Type SET description = ? WHERE type_id = ?"
            params = (description, type_id)
        else:
            query = "UPDATE Room_Type SET description = ?, max_guests = ? WHERE type_id = ?"
            params = (description, max_guests, type_id)
        cursor = self.db.execute(query, params)
        return True

    def access_room_occupancy_by_type(self):
        """
        Fetches data for occupancy rates by room type.
        Assumes tables: Booking, Room, Room_Type.
        And columns: Room_Type.description, Room.type_id (foreign key to Room_Type), Booking.room_id.
        """
        query = """
            SELECT RT.description AS room_type, COUNT(B.booking_id) AS booking_count
            FROM Booking B
            JOIN Room R ON B.room_id = R.room_id
            JOIN Room_Type RT ON R.type_id = RT.type_id -- Changed R.room_type_id to R.type_id
            GROUP BY RT.description
            ORDER BY booking_count DESC;
        """
        return self.db.fetchall(query)





