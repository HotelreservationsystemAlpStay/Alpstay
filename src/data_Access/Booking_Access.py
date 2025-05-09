import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.Validator import Validator
from models.Booking import Booking
from data_Access.Base_Access_Controller import Base_Access_Controller
from datetime import date, datetime
from controller.User_Controller import User_Controller
from mythic.mythic_code import Mythic


class Booking_Access:
    def __init__(self): 
        self.db = Base_Access_Controller()

    def create_booking(self, booking_id: int, check_in_date: date, check_out_date: date, is_cancelled: bool, total_amount: float, guest_id: int, room_id: int) -> Booking:
        """
        Create a new booking and save it to the database.
        
        Args:
            booking_id (int): The ID of the booking.
            check_in_date (date): The check-in date.
            check_out_date (date): The check-out date.
            is_cancelled (bool): Whether the booking is cancelled or not.
            guest_id (int): The ID of the guest.
            room_id (int): The ID of the room.

        Returns:
            Booking: The created booking object.
        """
        Validator.checkID(booking_id, "Booking ID")
        Validator.checkDateFormat(check_in_date, "Check-in date")
        Validator.checkDateFormat(check_out_date, "Check-out date")
        Validator.checkDates(check_in_date, check_out_date)
        Validator.checkBoolean(is_cancelled, "is_cancelled")
        Validator.checkID(guest_id, "Guest ID")
        Validator.checkID(room_id, "Room ID")

        booking = Booking(booking_id, check_in_date, check_out_date, is_cancelled, total_amount, guest_id, room_id)
        
        query = """
        INSERT INTO bookings (booking_id, check_in_date, check_out_date, is_cancelled, total_amount, guest_id, room_id) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        self.db.execute(query, (booking.booking_id, booking.check_in_date, booking.check_out_date, booking.is_cancelled, booking.total_amount, booking.guest_id, booking.room_id))
        
        return booking

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

    def get_all_bookings_and_hotels(self) -> list:
        query = """
        SELECT b.booking_id, b.check_in_date, b.check_out_date, b.is_cancelled, b.total_amount,
               b.guest_id, h.name, h.stars r.room_id
        FROM Booking b
        JOIN Room r ON b.room_id = r.room_id
        JOIN Hotel h ON r.hotel_id = h.hotel_id
        """
        rows = self.db.fetchall(query)
        results = []
        for row in rows:
            results.append({
                "booking": Booking(
                    row["booking_id"],
                    datetime.strptime(row["check_in_date"], "%Y-%m-%d").date(),
                    datetime.strptime(row["check_out_date"], "%Y-%m-%d").date(),
                    bool(row["is_cancelled"]),
                    row["total_amount"],
                    row["guest_id"],
                    row["room_id"]
                ),
                "hotel": {
                    "hotel_id": row["hotel_id"],
                    "name": row["name"],
                    "stars": row["stars"]
                }
            })
        return results

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
        vw = User_Controller()
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




us3 = Booking_Access()
us3.view_booking(6, "admin")




