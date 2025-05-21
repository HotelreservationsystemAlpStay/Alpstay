from datetime import datetime

class Rating:
    def __init__(self, rating_id: int, invoice, hotel, score: int, review: str = None, created_at: datetime = None):
        self._rating_id = rating_id
        self._invoice = invoice
        self._hotel = hotel
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
    def invoice(self):
        return self._invoice

    @invoice.setter
    def invoice(self, invoice) -> None:
        self._invoice = invoice

    @property
    def hotel(self):
        return self._hotel

    @hotel.setter
    def hotel(self, hotel) -> None:
        self._hotel = hotel

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
    
    def is_valid_score(self) -> bool:
        """
        Checks if the score is between 1 and 5.
        """
        return 1 <= self._score <= 5
    
    def update_score(self, new_score: int):
        """
        Updates the score.
        
        :param new_score: New score.
        """
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
            'rating_id': self._rating_id,
            'invoice': self._invoice.to_dict() if hasattr(self._invoice, "to_dict") else str(self._invoice),
            'hotel': self._hotel.to_dict() if hasattr(self._hotel, "to_dict") else str(self._hotel),
            'score': self._score,
            'review': self._review,
            'created_at': self._created_at.isoformat() if self._created_at else None
        }
    
    def __str__(self):
        return f"Rating(id={self._rating_id}, score={self._score}, review={self._review})"