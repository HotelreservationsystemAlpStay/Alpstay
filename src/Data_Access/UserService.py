import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.User import User
from Base_Access_Controller import Base_Access_Controller
import sqlite3


class UserService:
    def __init__(self):
        self.db_controller = Base_Access_Controller()

    def _sqlite3rowToUser(self, row: sqlite3.Row) -> User:
        return User(
            id=row["user_id"],
            guest_id=row["guest_id"],
            password=row["user_password"],
            role=row["user_role"],
        )

    def get_all_users(self) -> list[User]:
        user_data = self.db_controller.fetchall("SELECT * FROM User")
        user = []
        for row in user_data:
            user.append(self._sqlite3rowToUser(row))
        return user


u = UserService()
users = u.get_all_users()
for item in users:
    print(str(item))