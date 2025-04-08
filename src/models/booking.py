from datetime import date
from typing import Optional

class Booking:
    def __init__(self, booking_id: int, check_in_date: date, check_out_date: date, is_cancelled: bool, 
                 guest_id: int, room_id: int):
        self._booking_id = booking_id
        self._check_in_date = check_in_date
        self._check_out_date = check_out_date
        self._is_cancelled = is_cancelled
        self._guest_id = guest_id  # Foreign key to Guest
        self._room_id = room_id    # Foreign key to Room
        self._invoice = None       # Optional relationship to Invoice

    @property
    def booking_id(self) -> int:
        """Get the booking ID (read-only)."""
        return self._booking_id

    @property
    def check_in_date(self) -> date:
        """Get or set the check-in date."""
        return self._check_in_date

    @check_in_date.setter
    def check_in_date(self, value: date) -> None:
        if value >= self._check_out_date:
            raise ValueError("Check-in date must be before check-out date.")
        self._check_in_date = value

    @property
    def check_out_date(self) -> date:
        """Get or set the check-out date."""
        return self._check_out_date

    @check_out_date.setter
    def check_out_date(self, value: date) -> None:
        if value <= self._check_in_date:
            raise ValueError("Check-out date must be after check-in date.")
        self._check_out_date = value

    @property
    def is_cancelled(self) -> bool:
        """Get the cancellation status (read-only)."""
        return self._is_cancelled

    @property
    def guest_id(self) -> int:
        """Get or set the guest ID."""
        return self._guest_id

    @guest_id.setter
    def guest_id(self, value: int) -> None:
        if value <= 0:
            raise ValueError("Guest ID must be a positive integer.")
        self._guest_id = value

    @property
    def room_id(self) -> int:
        """Get or set the room ID."""
        return self._room_id

    @room_id.setter
    def room_id(self, value: int) -> None:
        if value <= 0:
            raise ValueError("Room ID must be a positive integer.")
        self._room_id = value

    @property
    def invoice(self) -> Optional[int]:
        """Get or set the associated invoice ID."""
        return self._invoice

    @invoice.setter
    def invoice(self, value: Optional[int]) -> None:
        if value is not None and value <= 0:
            raise ValueError("Invoice ID must be a positive integer.")
        self._invoice = value

    def calculate_total_days(self) -> int:
        """
        Calculate the total number of days for the booking.
        
        Returns:
            int: The number of days between check-in and check-out.
        """
        return (self._check_out_date - self._check_in_date).days

    def associate_invoice(self, invoice_id: int):
        """
        Associate an invoice with this booking.
        
        Args:
            invoice_id (int): The ID of the invoice to associate.
        """
        self.invoice = invoice_id

    def cancel_booking(self):
        """
        Mark the booking as cancelled.
        
        This sets the `is_cancelled` attribute to True.
        """
        self._is_cancelled = True
    
    def __str__(self):
        """
        Return a string representation of the booking.
        
        Returns:
            str: A string containing all booking details.
        """
        return (f"Booking(booking_id={self._booking_id}, check_in_date={self._check_in_date}, "
                f"check_out_date={self._check_out_date}, is_cancelled={self._is_cancelled}, "
                f"guest_id={self._guest_id}, room_id={self._room_id}, invoice={self._invoice})")