import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data_Access.Base_Access_Controller import Base_Access_Controller
from datetime import date
from models.Invoicecorrected import Invoice


class Invoice_Access:
    def __init__(self):
        self.db = Base_Access_Controller()
    
    def get_booking_details(self, booking_id):
        query = """
        SELECT check_in_date, check_out_date, is_cancelled, total_amount, first_name, last_name, name, price_per_night
        FROM booking_view 
        WHERE booking_id = ?
        """
        return self.db.execute(query, booking_id)
        
    
    def access_invoice(self, booking_id, issue_date):
        query = """
        SELECT name, hotel_id, stars, first_name, last_name, check_in_date, check_out_date, total_amount
        FROM booking_view
        WHERE booking_id = ?
        """
        result = self.db.fetchone(query, (booking_id,))

        query_insert = """
                INSERT INTO Invoice (booking_id, issue_date, total_amount)
                VALUES (?, ?, ?)
                """
        self.db.execute(query_insert, (invoice._invoice_id,invoice.booking_id, invoice.issue_date, invoice.total_amount))
        invoice_id = self.db.cursor.lastrowid
        return

    


    
