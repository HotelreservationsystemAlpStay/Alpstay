from datetime import date
from typing import Optional

class Booking:
    def __init__(self, booking_id: int, check_in_date: date, check_out_date: date, is_cancelled: bool, 
                 guest_id: int, room_id: int):
        self.booking_id = booking_id
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.is_cancelled = is_cancelled
        self.guest_id = guest_id  # Foreign key to Guest
        self.room_id = room_id    # Foreign key to Room
        self.invoice = None       # Optional relationship to Invoice

    def calculate_total_days(self) -> int:
        """
        Calculate the total number of days for the booking.
        
        Returns:
            int: The number of days between check-in and check-out.
        """
        return (self.check_out_date - self.check_in_date).days

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
        self.is_cancelled = True
    
    def __str__(self):
        """
        Return a string representation of the booking.
        
        Returns:
            str: A string containing all booking details.
        """
        return (f"Booking(booking_id={self.booking_id}, check_in_date={self.check_in_date}, "
                f"check_out_date={self.check_out_date}, is_cancelled={self.is_cancelled}, "
                f"guest_id={self.guest_id}, room_id={self.room_id}, invoice={self.invoice})")