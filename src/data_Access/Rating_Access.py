import sys
import os
from datetime import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data_Access.Base_Access_Controller import Base_Access_Controller
from models.Rating import Rating

class RatingAccess:
    def __init__(self): 
        self.db = Base_Access_Controller()

    def create_rating(self, hotel_id: int, guest_id: int, score: int, comment: str, created_at: datetime):

        query_max_id = """
            SELECT MAX(rating_id) FROM Rating
        """
        result_max = self.db.fetchone(query_max_id)[0]
        if result_max is None:
            result_max = 0

        sql = """
            INSERT INTO Rating VALUES(?, ?, ?, ?, ?, ?)
        """

        c = self.db.execute(sql, tuple([result_max+1, hotel_id, guest_id, score, comment, created_at.timestamp()]))
        row_id = c.lastrowid
        return Rating(row_id, hotel_id, guest_id, score, comment) # TODO: created_at to model
    
    def create_rating_new(self, booking_id, hotel_id, score, review, created_at):
        query = """
        INSERT INTO Rating (booking_id, hotel_id, score, review, created_at)
        VALUES (?, ?, ?, ?, ?)
        """
        params = (booking_id, hotel_id, score, review, created_at)
        status = self.db.execute(query, params)
        if status.rowcount == 1:
            return True
        else:
            return False

    def get_rating_by_booking_id(self, booking_id: int) -> bool:
        """
        Checks if a rating for the given booking_id already exists.
        Returns True if a rating exists, False otherwise.
        """
        query = "SELECT * FROM Rating WHERE booking_id = ?"
        result = self.db.fetchone(query, (booking_id,))
        if result is None:
            return False
        else:
            return True

if __name__ == "__main__":
    ra = RatingAccess()
    r = ra.create_rating(1, 1, 3, "War super", datetime.now())
    print(r)