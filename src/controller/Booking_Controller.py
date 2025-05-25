from models.User import User
from models.Room import Room
from models.Booking import Booking
from models.Hotels import Hotel
from datetime import datetime
from data_Access.Booking_Access import Booking_Access

class Booking_Controller:
    def __init__(self):
        self.Booking_Access = Booking_Access()
    
    def create_booking(self, user:User, room:Room, startDate:datetime, endDate:datetime):
        delta = (endDate-startDate).days
        booking = Booking_Access().create_booking(check_in_date=startDate, check_out_date=endDate, is_cancelled=False, total_amount=delta*room.price_per_night, guest_id=user.guest_id, room_id=room.room_id)
        if booking:
            return booking
        return None
    
    def get_bookings_from_user(self, guest_id:int):
        return Booking_Access().access_booking_guest(guest_id=guest_id)
    
    def update_booking(self, booking:Booking, type:str):
        match type:
            case "cancel":
                Booking_Access().cancel_booking(booking_id=booking.booking_id)
                return True
            case _:
                pass

    def get_all_bookings(self):
        result = self.Booking_Access.access_all_booking()
        bookings = []
        for row in result:
            hotel = Hotel(row["hotel_id"], row["name"], row["stars"])
            booking = Booking(row["booking_id"], row["check_in_date"], row["check_out_date"], row["is_cancelled"], row["total_amount"], row["guest_id"], row["room_id"])
            bookings.append((hotel, booking))
        return bookings
