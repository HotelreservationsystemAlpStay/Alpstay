from utils.Validator import Validator
from data_Access.Base_Access_Controller import Base_Access_Controller
from data_Access.RoomType_Access import RoomType_Access
from controller.User_Controller import User_Controller
from models.RoomType import RoomType

class RoomType_Controller():
    def __init__(self):
        self.roomType_Access = RoomType_Access() 

    def get_all_roomtypes(self, hotels=[]):
        return self.roomType_Access.get_all_roomtypes(hotels=hotels)

    def get_roomType_by_id(self, id):
        return self.roomType_Access.get_roomtype_by_id(id)

    def add_roomType(self, user_id:int, password:str, description:str, max_guests:int):
        user_Controller = User_Controller()
        if not user_Controller.check_admin(user_id, password):
            return False
        return self.roomType_Access.add_roomtype(description, max_guests) 
            

    def modify_roomType(self, roomType:RoomType, description:str=None, max_guests:int=None):
        return self.roomType_Access.modify_roomtype(roomType.id, description, max_guests)

    def get_room_occupancy_data(self):
        """
        Prepares data for occupancy rates by room type chart.
        Expected format for ChartView: {'room_type': [...], 'count': [...]}
        """
        raw_data = self.roomType_Access.access_room_occupancy_by_type()
        if not raw_data:
            return {'room_type': [], 'count': []}
        
        room_types = [row['room_type'] for row in raw_data]
        counts = [row['booking_count'] for row in raw_data]
        return {'room_type': room_types, 'count': counts}