import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data_Access.Base_Access_Controller import Base_Access_Controller
from models.User import User
import hashlib

class User_Controller:
    def __init__(self):
        self.db = Base_Access_Controller()

    def check_admin(self, user_id, password):
        query = """
        SELECT *
        FROM User
        WHERE user_id = ?
        """
        result = self.db.fetchone(query,(user_id,))
        if result is None:
            raise ValueError("We couldnt find your user_id, please try again")
        data = dict(result)
        user = User(id = data["user_id"], guest_id = data["guest_id"], password = data["user_password"], role = data["user_role"])
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        if user.password == password_hash: 
            if user.role == "Admin":
                print("Admin Access granted") #TBD
                return True
            elif user.role == "Guest":
                print("Guest Access granted") #TBD
                return False
            else:
                raise ValueError("User Role not defined, please contact the admin and report this issue")
        else: 
            raise ValueError("The password you entered is wrong, please try again")

#Test
test1 = User_Controller()
test1.check_admin(6, "admin")



