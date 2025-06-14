from models.Rating import Rating
from data_Access.Rating_Access import RatingAccess
from datetime import date
from utils.Validator import Validator


class RatingManager:
    def __init__(self):
        """Initialize Rating Manager with Rating Access layer."""
        self.rating_Access = RatingAccess()
    
    def create_rating(self, booking_id, hotel_id, score, review):
        """Create a new rating for a hotel booking.

        Args:
            booking_id: ID of the booking being rated
            hotel_id: ID of the hotel being rated
            score: Rating score (1-5)
            review: Written review text

        Returns:
            Status of rating creation

        Raises:
            ValueError: If score is not between 1-5 or rating already exists for booking
        """
        booking_id = int(booking_id)
        Validator.checkID(booking_id, "booking ID")
        hotel_id = int(hotel_id)
        Validator.checkID(hotel_id)
        score = int(score)
        if score > 5 or score < 1:
            raise ValueError("Score must be between 1 and 5")
        created_at = date.today()

        if self.rating_Access.get_rating_by_booking_id(booking_id):
            raise ValueError(f"For this BookingID -> {booking_id} already exists a rating.")

        status = self.rating_Access.create_rating_new(booking_id, hotel_id, score, review, created_at)
        return status
    
    def get_ratings_for_hotel(self, hotel_id_str: str) -> list[dict]:
        """
        Retrieves all ratings for a given hotel ID.
        """
        try:
            hotel_id = int(hotel_id_str)
            Validator.checkID(hotel_id, "Hotel ID")
        except (ValueError, TypeError):
            raise ValueError("Invalid hotel ID format. Please provide a valid integer.")
        
        ratings_data = self.rating_Access.get_ratings_by_hotel_id(hotel_id)
        return ratings_data
