import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from controller.DataBaseController import DataBaseController
from datetime import date
from models.Invoicecorrected import Invoice


class Invoiceservice:
    def __init__(self):
        self.db = DataBaseController()
    
    def create_invoice(self, booking_id):
        query = """
        SELECT name, first_name, last_name, street, city, price_per_night, check_in_date, check_out_date, total_amount
        FROM booking_view
        WHERE booking_id = ?
        """
        query_max = """
        SELECT MAX(invoice_id)
        FROM Invoice
        """
        result = self.db.fetchone(query, (booking_id,))
        result_max = self.db.fetchone(query_max)[0] #0 sagt hier, nimm den ersten Wert aus der Tupel
        data = dict(result)
        total_amount = data["total_amount"]
        invoice = Invoice(invoice_id = result_max+1, booking_id = booking_id, issue_date = date.today(), total_amount = total_amount)
        query_insert = """
                INSERT INTO Invoice (invoice_id, booking_id, issue_date, total_amount)
                VALUES (?, ?, ?, ?)
                """
        self.db.execute(query_insert, (invoice._invoice_id,invoice.booking_id, invoice.issue_date, invoice.total_amount))
        print("Invoice was generated successfuly")
        #Achtung ich hole hier noch extrem viele unnötige Parameter, ich möchte vielleicht die Story noch erweitern um ein PDF mit diesen Parametern zu erstellen, deshalb bitte nicht ändern

#Test
test = Invoiceservice()
test.create_invoice(2)
