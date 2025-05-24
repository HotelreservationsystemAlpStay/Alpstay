import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data_Access.Base_Access_Controller import Base_Access_Controller
from datetime import date
from models.Invoicecorrected import Invoice


class Invoice_Access:
    def __init__(self):
        self.db = Base_Access_Controller()
    
    def get_booking_details(self, booking_id:int):
        query = """
        SELECT hotel_id, stars, check_in_date, check_out_date, is_cancelled, total_amount, first_name, last_name, name, guest_id, room_id
        FROM booking_view 
        WHERE booking_id = ?
        """
        return self.db.fetchone(query, (booking_id,))
        
    
    def create_invoice(self, booking_id, issue_date, total_amount):
        query_insert = """
        INSERT INTO Invoice (booking_id, issue_date, total_amount)
        VALUES (?, ?, ?)
        """
        params = (booking_id, issue_date, total_amount)
        result = self.db.execute(query_insert, params)
        generated_id = result.lastrowid
        return generated_id


    
