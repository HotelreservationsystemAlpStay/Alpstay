from datetime import date
from typing import Optional
from pydantic import BaseModel, field_validator, model_validator

class BookingPydantic(BaseModel):
    booking_id: int
    check_in_date: date
    check_out_date: date
    is_cancelled: bool = False
    guest_id: int
    room_id: int
    invoice: Optional[int] = None

    @model_validator
    def check_dates(cls, values):
        check_in = values.get('check_in_date')
        check_out = values.get('check_out_date')
        if check_in and check_out and check_in >= check_out:
            raise ValueError("Check-in date must be before check-out date.")
        return values

    @field_validator('guest_id', 'room_id')
    def ensure_positive(cls, v):
        if v <= 0:
            raise ValueError("Guest ID and Room ID must be positive integers.")
        return v

    @field_validator('invoice', always=True)
    def validate_invoice(cls, v):
        if v is not None and v <= 0:
            raise ValueError("Invoice ID must be a positive integer.")
        return v

    def calculate_total_days(self) -> int:
        """
        Calculate the total number of days for the booking.
        """
        return (self.check_out_date - self.check_in_date).days

    def cancel_booking(self):
        """
        Mark the booking as cancelled.
        """
        self.is_cancelled = True