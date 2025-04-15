from datetime import date

class Booking:
    def __init__(self, booking_id: int, check_in_date: date, check_out_date: date, is_cancelled: bool, 
                 guest_id: int, room_id: int):
        
        self._validate_booking_id(booking_id)
        self._validate_dates(check_in_date, check_out_date)
        self._validate_is_cancelled(is_cancelled)
        self._validate_guest_id(guest_id)
        self._validate_room_id(room_id)
        
        self.booking_id = booking_id
        self.check_in_date = check_in_date
        self._heck_out_date = check_out_date
        self.is_cancelled = is_cancelled
        self.guest_id = guest_id  # Foreign key to Guest
        self.room_id = room_id    # Foreign key to Room

    def _validate_booking_id(self, booking_id: int) -> None:
        if not isinstance(booking_id, int):
            raise TypeError("Booking ID must be an integer.")
        if booking_id <= 0:
            raise ValueError("Booking ID must be a positive integer.")

    def _validate_dates(self, check_in_date: date, check_out_date: date) -> None:
        if not isinstance(check_in_date, date) or not isinstance(check_out_date, date):
            raise TypeError("Check-in and check-out dates must be date objects.")
        if check_in_date >= check_out_date:
            raise ValueError("Check-in date must be before check-out date.")

    def _validate_is_cancelled(self, is_cancelled: bool) -> None:
        if not isinstance(is_cancelled, bool):
            raise TypeError("is_cancelled must be a boolean.")

    def _validate_guest_id(self, guest_id: int) -> None:
        if not isinstance(guest_id, int):
            raise TypeError("Guest ID must be an integer.")
        if guest_id <= 0:
            raise ValueError("Guest ID must be a positive integer.")

    def _validate_room_id(self, room_id: int) -> None:
        if not isinstance(room_id, int):
            raise TypeError("Room ID must be an integer.")
        if room_id <= 0:
            raise ValueError("Room ID must be a positive integer.")

    def calculate_total_days(self) -> int:
        """
        Calculate the total number of days for the booking.
        
        Returns:
            int: The number of days between check-in and check-out.
        """
        return (self._check_out_date - self._check_in_date).days

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
