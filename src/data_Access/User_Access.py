import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.User import User
from data_Access.Base_Access_Controller import Base_Access_Controller
import sqlite3


class User_Access:
    def __init__(self):
        self.db_controller = Base_Access_Controller()

    @staticmethod
    def _sqlite3row_to_user(row: sqlite3.Row) -> User:
        return User(
            id=row["user_id"],
            guest_id=row["guest_id"],
            password=row["user_password"],
            role=row["user_role"],
        )

    def get_all_users(self) -> list[User]:
        user_data = self.db_controller.fetchall("SELECT * FROM User")
        users = []
        for row in user_data:
            users.append(self._sqlite3row_to_user(row))
        return users
    
    def get_user(self, user_id:int, password:str) -> None | User:
        """expects user_id and HASHED password as is in db, returns None if no result has been found, returns a user otherwise
        
        Args:
            user_id (int): user id as is in db
            password (str): hash as is in db
            
        Returns:
            None|User: as in description
        """
        query = """
        SELECT *
        FROM User
        WHERE user_id = ? 
        AND user_password = ?
        """
        result = self.db_controller.fetchone(query,(user_id,password))
        if not result:
            return None
        return self._sqlite3row_to_user(result)

if __name__ == "__main__":
    print(User_Access().get_user(1, "name"))