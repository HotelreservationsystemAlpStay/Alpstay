from data_Access.Base_Access_Controller import Base_Access_Controller
from utils.Formatting import Format
from models.Booking import Booking
from models.Hotels import Hotel


class Invoice_Access:
    def __init__(self):
        """Initialize Invoice Access with database controller."""
        self.db = Base_Access_Controller()
    
    def get_booking_details(self, booking_id:int):
        """Get booking details for invoice generation.

        Args:
            booking_id (int): ID of the booking

        Returns:
            Tuple of hotel, booking, first_name, last_name, nights or 'no_booking' if not found
        """
        query = """
        SELECT hotel_id, stars, check_in_date, check_out_date, is_cancelled, total_amount, first_name, last_name, name, guest_id, room_id
        FROM booking_view 
        WHERE booking_id = ?
        """
        try:
            data = dict(self.db.fetchone(query, (booking_id,)))
            hotel = Hotel(data["hotel_id"], data["name"], data["stars"])
            check_in = Format.parse(data["check_in_date"])
            check_out = Format.parse(data["check_out_date"])
            booking = Booking(booking_id, check_in, check_out, bool(data["is_cancelled"]), data["total_amount"], data["guest_id"], data["room_id"])
            nights = (check_out - check_in).days
            return hotel, booking, data["first_name"], data["last_name"], nights
        except:
            return "no_booking"
        
    
    def create_invoice(self, booking_id, issue_date, total_amount):
        """Create a new invoice in the database.

        Args:
            booking_id: ID of the associated booking
            issue_date: Date the invoice was issued
            total_amount: Total amount for the invoice

        Returns:
            Invoice ID if successful
        """
        query_insert = """
        INSERT INTO Invoice (booking_id, issue_date, total_amount)
        VALUES (?, ?, ?)
        """
        params = (booking_id, issue_date, total_amount)
        result = self.db.execute(query_insert, params)
        generated_id = result.lastrowid
        return generated_id



