import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data_Access.Base_Access_Controller import Base_Access_Controller
from data_Access.User_Access import User_Access
from models.User import User
import hashlib

class User_Controller:
    def __init__(self):
        self.ua = User_Access()


    def check_admin(self, user_id, password):
        user_return = self.ua.get_user(user_id=user_id, password=hashlib.sha256(password.encode()).hexdigest())
        if not user_return or user_return['user_role'] != "Admin":
            return False
        return True


