import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data_Access.RoomType_Access import RoomType_Access
from controller.User_Controller import User_Controller

class RoomType_Controller():
    def __init__(self):
        pass

    def add_roomType(self, user_id:int, password:str, description:str=None, max_guest:int=None):
        user_Controller = User_Controller()
        if not user_Controller(user_id, password):
            return True
        else:
            return False


