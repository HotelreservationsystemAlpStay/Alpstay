from utils.Validator import Validator
from data_Access.Base_Access_Controller import Base_Access_Controller
from data_Access.Room_Type_Access import Room_Type_Access
from managers.User_Manager import User_Manager
from models.Room_Type import Room_Type

class Room_Type_Manager():
    def __init__(self):
        """Initialize Room Type Manager with Room Type Access layer."""
        self.room_Type_Access = Room_Type_Access() 

    def get_all_roomtypes(self, hotels=[]):
        """Get all room types with optional hotel filter.

        Args:
            hotels (list, optional): List of hotels to filter by

        Returns:
            List of room types
        """
        return self.room_Type_Access.get_all_Room_Types(hotels=hotels)

    def get_roomType_by_id(self, id):
        """Get room type by ID.

        Args:
            id: Room type ID

        Returns:
            Room type object
        """
        return self.room_Type_Access.get_Room_Type_by_id(id)

    def add_roomType(self, user_id:int, password:str, description:str, max_guests:int):
        """Add a new room type (admin only).

        Args:
            user_id (int): User ID for admin verification
            password (str): Password for admin verification
            description (str): Description of the room type
            max_guests (int): Maximum number of guests

        Returns:
            bool: True if successful, False if not admin or failed
        """
        user_Manager = User_Manager()
        if not user_Manager.check_admin(user_id, password):
            return False
        return self.room_Type_Access.add_Room_Type(description, max_guests) 
            

    def modify_roomType(self, roomType:Room_Type, description:str=None, max_guests:int=None):
        """Modify an existing room type.

        Args:
            roomType (Room_Type): Room type to modify
            description (str, optional): New description
            max_guests (int, optional): New maximum guest count

        Returns:
            Updated room type object
        """
        return self.room_Type_Access.modify_Room_Type(roomType.id, description, max_guests)

    def get_room_occupancy_data(self):
        """
        Prepares data for occupancy rates by room type chart.
        Expected format for ChartView: {'room_type': [...], 'count': [...]}
        """
        raw_data = self.room_Type_Access.access_room_occupancy_by_type()
        if not raw_data:
            return {'room_type': [], 'count': []}
        
        room_types = [row['room_type'] for row in raw_data]
        counts = [row['booking_count'] for row in raw_data]
        return {'room_type': room_types, 'count': counts}
