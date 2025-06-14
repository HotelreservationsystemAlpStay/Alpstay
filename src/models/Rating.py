from datetime import datetime

class Rating:
    def __init__(self, rating_id: int, booking_id: int, hotel_id: int, score: int, review: str = None, created_at: datetime = None):
        """Initialize a Rating with id, booking/hotel references, score, and optional review."""
        self._rating_id = rating_id
        self._booking_id = booking_id
        self._hotel_id = hotel_id
        self._score = score
        self._review = review
        self._created_at = created_at if created_at is not None else datetime.now()

    @property
    def rating_id(self) -> int:
        """Get the rating ID."""
        return self._rating_id

    @rating_id.setter
    def rating_id(self, rating_id: int) -> None:
        """Set the rating ID."""
        self._rating_id = rating_id

    @property
    def booking_id(self) -> int:
        """Get the booking ID."""
        return self._booking_id

    @booking_id.setter
    def booking_id(self, booking_id: int) -> None:
        """Set the booking ID."""
        self._booking_id = booking_id

    @property
    def hotel_id(self) -> int:
        """Get the hotel ID."""
        return self._hotel_id

    @hotel_id.setter
    def hotel_id(self, hotel_id: int) -> None:
        """Set the hotel ID."""
        self._hotel_id = hotel_id

    @property
    def score(self) -> int:
        """Get the rating score."""
        return self._score

    @score.setter
    def score(self, score: int) -> None:
        """Set the rating score."""
        self._score = score

    @property
    def review(self) -> str:
        """Get the review text."""
        return self._review

    @review.setter
    def review(self, review: str) -> None:
        """Set the review text."""
        self._review = review

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: datetime) -> None:
        self._created_at = created_at
        
    def to_dict(self) -> dict:
        """
        Serializes the Rating instance into a dictionary.
        """
        return {
            'rating_id': self._rating_id,
            'booking_id': self._booking_id,
            'hotel_id': self._hotel_id,
            'score': self._score,
            'review': self._review,
            'created_at': self._created_at.isoformat() if self._created_at else None
        }

    
    def __str__(self):
        return f"Rating(id={self._rating_id}, booking_id={self._booking_id}, hotel_id={self._hotel_id}, score={self._score}, review={self._review})"
