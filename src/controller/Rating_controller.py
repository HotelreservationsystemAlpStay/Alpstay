from models.Rating import Rating
from data_Access.Rating_Access import RatingAccess
from datetime import date
from utils.Validator import Validator


class RatingController:
    def __init__(self):
        self.rating_Access = RatingAccess()
    
    def create_rating(self, booking_id, hotel_id, score, review):
        booking_id = int(booking_id)
        Validator.checkID(booking_id, "booking ID")
        hotel_id = int(hotel_id)
        Validator.checkID(hotel_id)
        score = int(score)
        if score > 5 or score < 1:
            raise ValueError("Score must be between 1 and 5")
        created_at = date.today()
        status = self.rating_Access.create_rating_new(booking_id, hotel_id, score, review, created_at)
        return status
    