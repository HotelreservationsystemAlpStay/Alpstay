import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
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
        result = self.invoice_access.get_booking_details(booking_id)
        hotel, booking, first_name, last_name, nights = result
        if booking.is_cancelled:
            return "cancelled"
        issue_date = Format.date_to_string(date.today())
        invoice_id = self.invoice_access.create_invoice(booking_id, issue_date, booking.total_amount)
        if invoice_id:
            invoice = Invoice(invoice_id, booking_id, issue_date, booking.total_amount)
            return hotel, invoice, booking, first_name, last_name, nights
        return False
            

        
