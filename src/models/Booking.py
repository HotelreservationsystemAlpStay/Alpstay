from datetime import date

class Booking:
    def __init__(self, booking_id: int, check_in_date: date, check_out_date: date, is_cancelled: bool, 
                 total_amount: float, guest_id: int, room_id: int, telefon:int=None):
        """Initialize a Booking with all necessary details."""
        
        self._booking_id = booking_id
        self._check_in_date = check_in_date
        self._check_out_date = check_out_date 
        self._is_cancelled = is_cancelled
        self._total_amount = total_amount 
        self._guest_id = guest_id
        self._room_id = room_id
        self._telefon = telefon

    @property
    def booking_id(self) -> int:
        """Get the booking ID."""
        return self._booking_id

    @booking_id.setter
    def booking_id(self, booking_id: int) -> None:
        """Set the booking ID."""
        self._booking_id = booking_id

    @property
    def check_in_date(self) -> date:
        """Get the check-in date."""
        return self._check_in_date

    @check_in_date.setter
    def check_in_date(self, check_in_date: date) -> None:
        """Set the check-in date."""
        self._check_in_date = check_in_date

    @property
    def check_out_date(self) -> date:
        """Get the check-out date."""
        return self._check_out_date

    @check_out_date.setter
    def check_out_date(self, check_out_date: date) -> None:
        """Set the check-out date."""
        self._check_out_date = check_out_date

    @property
    def is_cancelled(self) -> bool:
        """Get the cancellation status."""
        return self._is_cancelled

    @is_cancelled.setter
    def is_cancelled(self, is_cancelled: bool) -> None:
        """Set the cancellation status."""
        self._is_cancelled = is_cancelled
        
    @property
    def total_amount(self) -> float:
        """Get the total booking amount."""
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount: float) -> None:
        """Set the total booking amount."""
        self._total_amount = total_amount

    @property
    def guest_id(self) -> int:
        """Get the guest ID."""
        return self._guest_id

    @guest_id.setter
    def guest_id(self, guest_id: int) -> None:
        """Set the guest ID."""
        self._guest_id = guest_id

    @property
    def room_id(self) -> int:
        """Get the room ID."""
        return self._room_id

    @room_id.setter
    def room_id(self, room_id: int) -> None:
        """Set the room ID."""
        self._room_id = room_id

    @property
    def telefon(self)->int:
        """Get the telefon number."""
        return self._telefon
    
    @telefon.setter
    def telefon(self, telefon:int):
        """Set the telefon number."""
        self._telefon = telefon
    
    def __str__(self):
        """
        Return a string representation of the booking.
        
        Returns:
            str: A string containing all booking details.
        """
        return (f"Booking(booking_id={self._booking_id}, check_in_date={self._check_in_date}, "
                f"check_out_date={self._check_out_date}, is_cancelled={self._is_cancelled}, "
                f"total_amount={self._total_amount}, guest_id={self._guest_id}, room_id={self._room_id})")
    
    def to_dict(self) -> dict:
        return {
            'booking_id': self._booking_id,
            'check_in_date': self._check_in_date.isoformat() if self._check_in_date else None,
            'check_out_date': self._check_out_date.isoformat() if self._check_out_date else None,
            'is_cancelled': self._is_cancelled,
            'total_amount': self._total_amount,
            'guest_id': self._guest_id,
            'room_id': self._room_id
        }