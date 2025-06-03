from models.Invoice import Invoice
from data_Access.Invoice_Access import Invoice_Access
from models.Hotels import Hotel
from datetime import date
from models.Booking import Booking
from utils.Formatting import Format


class Invoice_Controller:
    def __init__(self):
        self.invoice_access = Invoice_Access()
    def create_invoice(self, booking_id):
        """Creates an invoice for a booking if it is not cancelled.

        Gets the booking details, checks if it was cancelled, and creates the invoice.
        Returns the hotel, invoice, booking, guest name, and number of nights if successful.

        Args:
            booking_id (int): ID of the booking

        Returns:
            str: "cancelled" if the booking was cancelled
            tuple: (Hotel, Invoice, Booking, first_name, last_name, nights) if successful
            bool: False if invoice creation failed
        """
        booking_details = self.invoice_access.get_booking_details(booking_id)
        data = dict(booking_details)
        is_cancelled = bool(data["is_cancelled"])
        first_name = data["first_name"]
        last_name = data["last_name"]
        hotel_id = data["hotel_id"]
        hotel_name = data["name"]
        hotel_stars = data["stars"]
        check_in_date = Format.parse(data["check_in_date"])
        check_out_date = Format.parse(data["check_out_date"])
        guest_id = data["guest_id"]
        room_id = data["room_id"]
        hotel = Hotel(hotel_id, hotel_name, hotel_stars)
        issue_date = date.today()
        issue_date = Format.date_to_string(issue_date)
        total_amount = data["total_amount"]
        nights = (check_out_date - check_in_date).days
        booking = Booking(booking_id, check_in_date, check_out_date, is_cancelled, total_amount, guest_id, room_id)
        if is_cancelled:
            return "cancelled"
        else:
            invoice_id = self.invoice_access.create_invoice(booking_id, issue_date, total_amount)
            if invoice_id:
                invoice = Invoice(invoice_id, booking_id, issue_date, total_amount)
                return hotel, invoice, booking, first_name, last_name, nights
            else:
                return False
        

        
