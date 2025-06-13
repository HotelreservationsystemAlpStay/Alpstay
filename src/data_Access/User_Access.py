from models.User import User
from data_Access.Base_Access_Controller import Base_Access_Controller
import sqlite3


class User_Access:
    def __init__(self):
        """Initialize User Access with database controller."""
        self.db_Manager = Base_Access_Controller()

    @staticmethod
    def _sqlite3row_to_user(row: sqlite3.Row) -> User:
        """Convert SQLite row to User object."""
        return User(
            id=row["user_id"],
            guest_id=row["guest_id"],
            password=row["user_password"],
            role=row["user_role"],
        )

    def get_all_users(self) -> list[User]:
        """Get all users from the database.

        Returns:
            list[User]: List of all users
        """
        user_data = self.db_Manager.fetchall("SELECT * FROM User")
        users = []
        for row in user_data:
            users.append(self._sqlite3row_to_user(row))
        return users
    
    def get_user(self, user_id:int, password:str) -> None | User:
        """Get user by ID and hashed password.
        
        Args:
            user_id (int): user id as is in db
            password (str): hash as is in db
            
        Returns:
            None|User: User object if found, None otherwise
        """
        query = """
        SELECT *
        FROM User
        WHERE user_id = ? 
        AND user_password = ?
        """
        result = self.db_Manager.fetchone(query,(user_id,password))
        if not result:
            return None
        return self._sqlite3row_to_user(result)
    
    def get_user_by_guest_id(self, user_id):
        """Get guest ID by user ID.

        Args:
            user_id: The user ID to look up

        Returns:
            Guest ID if found, False otherwise
        """
        query = """
        SELECT guest_id 
        FROM User
        WHERE user_id = ?
        """
        result = self.db_Manager.fetchone(query, (user_id,))
        if result:
            return result["guest_id"]
        else:
            return False

if __name__ == "__main__":
    print(User_Access().get_user(1, "name"))