from models.Invoice import Invoice
from data_Access.Invoice_Access import Invoice_Access
from models.Hotels import Hotel
from datetime import date
from models.Booking import Booking
from utils.Formatting import Format
import requests


class Invoice_Manager:
    def __init__(self):
        self.invoice_access = Invoice_Access()

    def create_invoice(self, booking_id, e_mail = None):
        result = self.invoice_access.get_booking_details(booking_id)
        hotel, booking, first_name, last_name, nights = result
        if booking.is_cancelled:
            return "cancelled"
        issue_date = Format.date_to_string(date.today())
        try:
            invoice_id = self.invoice_access.create_invoice(booking_id, issue_date, booking.total_amount)
            if invoice_id:
                invoice = Invoice(invoice_id, booking_id, issue_date, booking.total_amount)
            if e_mail:
                variables = {
                    "e_mail": e_mail,
                    "invoice_id": invoice.invoice_id,
                    "booking_id": booking.booking_id,
                    "issue_date": invoice._issue_date,
                    "total_amount": invoice.total_amount,
                    "hotel_name": hotel.name,
                    "hotel_id": hotel.hotel_id,
                    "guest_first_name": first_name,
                    "guest_last_name": last_name,
                    "nights": nights
                }
                requests.post("https://hook.eu2.make.com/s61v18jmdy7n2pewspfdops7p26jgl6r", json=variables)
            return hotel, invoice, booking, first_name, last_name, nights
        except:
            return "no_booking"
        return False

            

        
