import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.Validator import Validator
from data_Access.Base_Access_Controller import Base_Access_Controller
from data_Access.RoomType_Access import RoomType_Access
from controller.User_Controller import User_Controller

class RoomType_Controller():
    def __init__(self):
        pass 

    def add_roomType(self, user_id:int, password:str, description:str, max_guests:int):
        user_Controller = User_Controller()
        if not user_Controller.check_admin(user_id, password):
            return False
        roomType_Access = RoomType_Access()
        return roomType_Access.add_roomtype()
            

    def modify_roomType(self, user_id:int, password:str, description:str=None, max_guests:int=None, type_id):
        user_Controller = User_Controller()
        if not user_Controller.check_admin(user_id, password):
            return False
        roomType_Access = RoomType_Access()
        return roomType_Access.modify_roomtype()