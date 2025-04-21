from datetime import datetime

class Rating:
    def __init__(self, rating_id: int, invoice, hotel, score: int, review: str = None, created_at: datetime = None):
        self._validate_rating_id(rating_id)
        self._validate_score(score)
        self._validate_review(review)
        self._validate_created_at(created_at)
        
        self.rating_id = rating_id
        self.invoice = invoice
        self.hotel = hotel
        self.score = score
        self.review = review
        self.created_at = created_at if created_at else datetime.now()
    
    def _validate_rating_id(self, rating_id: int) -> None:
        if not isinstance(rating_id, int):
            raise TypeError("Rating ID must be an integer.")
        if rating_id <= 0:
            raise ValueError("Rating ID must be a positive number.")

    def _validate_score(self, score: int) -> None:
        if not isinstance(score, int):
            raise TypeError("Score must be an integer.")
        if not 1 <= score <= 5:
            raise ValueError("Score must be between 1 and 5.")

    def _validate_review(self, review: str) -> None:
        if review is not None and not isinstance(review, str):
            raise TypeError("Review must be a string.")

    def _validate_created_at(self, created_at: datetime) -> None:
        if created_at is not None and not isinstance(created_at, datetime):
            raise TypeError("created_at must be a datetime object.")
    
    def is_valid_score(self) -> bool:
        """
        Checks if the score is between 1 and 5.
        """
        return 1 <= self.score <= 5
    
    def update_score(self, new_score: int):
        """
        Updates the score if the new value is valid.
        
        :param new_score: New score (must be between 1 and 5).
        :raises ValueError: If new_score is invalid.
        """
        self._validate_score(new_score)
        self.score = new_score
    
    def add_review(self, review_text: str):
        """
        Adds or updates a review comment.
        
        :param review_text: The text of the review.
        """
        self.review = review_text
        
    def to_dict(self) -> dict:
        """
        Serializes the Rating instance into a dictionary.
        """
        return {
            'rating_id': self.rating_id,
            'invoice': self.invoice.to_dict() if hasattr(self.invoice, "to_dict") else str(self.invoice),
            'hotel': self.hotel.to_dict() if hasattr(self.hotel, "to_dict") else str(self.hotel),
            'score': self.score,
            'review': self.review,
            'created_at': self.created_at.isoformat()
        }
    
    def __str__(self):
        return f"Rating(id={self.rating_id}, score={self.score}, review={self.review})"