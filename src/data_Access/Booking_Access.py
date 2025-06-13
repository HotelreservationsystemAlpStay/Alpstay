from utils.Validator import Validator
from models.Booking import Booking
from data_Access.Base_Access_Controller import Base_Access_Controller
from datetime import date, datetime
from managers.User_Manager import User_Manager
from mythic.mythic_code import Mythic
from sqlite3 import Cursor, Row

class Booking_Access:
    def __init__(self): 
        """Initialize Booking Access with database controller."""
        self.db = Base_Access_Controller()

    @staticmethod
    def _sqlite3row_to_booking(row:Row):
        """Convert SQLite row to Booking object."""
        return Booking(
            booking_id=row["booking_id"],
            guest_id=row["guest_id"],
            room_id=row["room_id"],
            check_in_date=row["check_in_date"],
            check_out_date=row["check_out_date"],
            is_cancelled=row["is_cancelled"],
            total_amount=row["total_amount"]
        )

    @staticmethod
    def _get_list_to_tuple(providedList:list):
        """Convert list to tuple."""
        return tuple(providedList)

    def create_booking(self, check_in_date: date, check_out_date: date, is_cancelled: bool, total_amount: float, guest_id: int, room_id: int) -> Booking:
        """
        Create a new booking and save it to the database.
        
        Args:
            check_in_date (date): The check-in date.
            check_out_date (date): The check-out date.
            is_cancelled (bool): Whether the booking is cancelled or not.
            guest_id (int): The ID of the guest.
            room_id (int): The ID of the room.

        Returns:
            Booking: The created booking object.
        """

        query = """
        INSERT INTO Booking (check_in_date, check_out_date, is_cancelled, total_amount, guest_id, room_id) 
        VALUES (?, ?, ?, ?, ?, ?)
        """
        result = self.db.execute(query, (check_in_date, check_out_date, is_cancelled, total_amount, guest_id, room_id))
        return self.get_booking(result.lastrowid)

    def get_booking(self, booking_id: int) -> Booking:
        Validator.checkID(booking_id, "Booking ID")
        query = "SELECT * FROM Booking WHERE booking_id=?"
        row = self.db.fetchone(query, (booking_id,))
        if row:
            return Booking(
                row["booking_id"],
                datetime.strptime(row["check_in_date"], "%Y-%m-%d").date(),
                datetime.strptime(row["check_out_date"], "%Y-%m-%d").date(),
                bool(row["is_cancelled"]),
                row["total_amount"],
                row["guest_id"],
                row["room_id"]
            )
        return None

    def access_all_booking(self):
        query="""
        SELECT hotel_id, name, stars, booking_id, check_in_date, check_out_date, is_cancelled, total_amount, guest_id, room_id
        FROM booking_view
        """
        return self.db.fetchall(query)

    def cancel_booking(self, booking_id: int):
        Validator.checkID(booking_id, "Booking ID")
        query_check_booking = """
        SELECT is_cancelled
        FROM Booking
        WHERE booking_id = ?
        """
        status = self.db.fetchone(query_check_booking,(booking_id,))[0]
        if status == 1:
            raise ValueError("This booking was already cancelled")
        query = """
                UPDATE Booking 
                SET is_cancelled=1, total_amount = 0
                WHERE booking_id=?
                """
        result = self.db.execute(query, (booking_id,))
        if result.rowcount == 0:
            raise ValueError("No booking with this Booking ID was found")
        query_invoice_id = """
        SELECT MAX(invoice_id) FROM Invoice
        """
        max_id = self.db.fetchone(query_invoice_id)[0]
        query_create_invoice = """
        INSERT INTO Invoice
        VALUES(?, ?, ?, ?)
        """
        self.db.execute(query_create_invoice, (max_id + 1, booking_id, date.today(), 0,))
        print("Booking was cancelled successfuly and created a matching invoice")

    def view_booking(self, user_id, password):
        db = Base_Access_Controller()
        vw = User_Manager()
        if vw.check_admin(user_id, password):
            mythic = Mythic()
            mythic.wtf()
        else:
            query = """
            SELECT check_in_date, check_out_date, name, total_amount, city, booking_id
            FROM booking_view
            WHERE guest_id = ?
            """
            result = self.db.fetchall(query, (user_id,))
            for row in result:
                data = dict(row)
                print(f"Booking NR: {data['booking_id']}, check-in: {data['check_in_date']}, check-out: {data['check_out_date']}, hotel: {data['name']}, cost: {data['total_amount']}")

    def access_booking_guest(self, guest_id):
        query = """
        SELECT * FROM Booking WHERE guest_id = ?
        """
        result = self.db.fetchall(query, (guest_id,))
        bookings = []
        for row in result:
            bookings.append(self._sqlite3row_to_booking(row))
        return bookings
    
    def update_booking(self, booking:Booking, phonenumber:int=None, iscancelled:bool=None, totalamount:int=None):
        query = "update Booking set "
        param = []
        if phonenumber:
            query += "telefon = ?"
            param.append(phonenumber)
        if iscancelled:
            query += "is_cancelled = ?"
            if iscancelled:
                param.append(1)
            else:
                param.append(0)
        query += " WHERE booking_id = ?"
        param.append(booking.booking_id)
        return self.db.execute(query, params=self._get_list_to_tuple(param))
    
    def check_user_id_matches_booking_id(self, booking_id, guest_id):
        query = """
        SELECT hotel_id
        FROM booking_view
        WHERE booking_id = ?
        AND guest_id = ?
        """
        params = (booking_id, guest_id)
        result = self.db.fetchone(query, params)
        return result







