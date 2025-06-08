from datetime import datetime

class Rating:
    def __init__(self, rating_id: int, booking_id: int, hotel_id: int, score: int, review: str = None, created_at: datetime = None):
        self._rating_id = rating_id
        self._booking_id = booking_id
        self._hotel_id = hotel_id
        self._score = score
        self._review = review
        self._created_at = created_at if created_at is not None else datetime.now()

    @property
    def rating_id(self) -> int:
        return self._rating_id

    @rating_id.setter
    def rating_id(self, rating_id: int) -> None:
        self._rating_id = rating_id

    @property
    def booking_id(self) -> int:
        return self._booking_id

    @booking_id.setter
    def booking_id(self, booking_id: int) -> None:
        self._booking_id = booking_id

    @property
    def hotel_id(self) -> int:
        return self._hotel_id

    @hotel_id.setter
    def hotel_id(self, hotel_id: int) -> None:
        self._hotel_id = hotel_id

    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, score: int) -> None:
        self._score = score

    @property
    def review(self) -> str:
        return self._review

    @review.setter
    def review(self, review: str) -> None:
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
