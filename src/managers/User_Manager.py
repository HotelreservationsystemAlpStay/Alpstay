from data_Access.Base_Access_Controller import Base_Access_Controller
from data_Access.User_Access import User_Access
from models.User import User
from utils.Validator import Validator
import hashlib

class User_Manager:
    def __init__(self):
        self.ua = User_Access()

    def login_user(self, user_id:int, password:str) -> None | User:
        """returns user if found in db, otherwise returns None

        Args:
            user_id (int): user id as is in db
            password (str): password unhashed

        Returns:
            None | User: as in description
        """
        return self.ua.get_user(user_id=user_id, password=hashlib.sha256(password.encode()).hexdigest())

    def check_admin(self, user_id:int, password:str) -> bool:
        """returns true if user with user_id and password exists in db, if user does not exists or password is incorrect, false shall be returned

        Args:
            user_id (int): user id as is in the db
            password (str): unhashes password

        Returns:
            bool: returns state as described
        """
        user_return = self.ua.get_user(user_id=user_id, password=hashlib.sha256(password.encode()).hexdigest())
        if not user_return or user_return.role != "Admin":
            return False
        return True

    def get_guest_id(self, user_id:int) -> int:
        user_id = int(user_id)
        Validator.checkID(user_id)
        guest_id = self.ua.get_user_by_guest_id(user_id)
        guest_id = int(guest_id)
        return guest_id




if __name__ == "__main__":
    print(User_Manager().check_admin(6,"admin")) #expected True
    print(User_Manager().check_admin(6,"admins")) #expected False