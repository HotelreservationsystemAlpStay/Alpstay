from models.User import User
from models.Room import Room
from models.Booking import Booking
from models.Hotels import Hotel
from datetime import datetime
from data_Access.Booking_Access import Booking_Access
from utils.Validator import Validator
from utils.Formatting import Format

class Booking_Manager:
    def __init__(self):
        self.Booking_Access = Booking_Access()
    
    def create_booking(self, user:User, room:Room, startDate:datetime, endDate:datetime):
        delta = (endDate-startDate).days
        booking = Booking_Access().create_booking(check_in_date=startDate, check_out_date=endDate, is_cancelled=False, total_amount=delta*room.price_per_night, guest_id=user.guest_id, room_id=room.room_id)
        if booking:
            return booking
        else:
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
    
    def update_booking(self, booking:Booking, phonenumber:int=None, iscancelled:bool=None, totalamount:int=None):
        self.Booking_Access.update_booking(self, booking, phonenumber, iscancelled, totalamount)
    
    def create_booking_new(self, guest_id, room_id, check_in_date, check_out_date, total_amount, telefon=None):
        guest_id = int(guest_id)
        room_id = int(room_id)
        Validator.checkID(guest_id, "guest ID")
        Validator.checkID(room_id, "room ID")
        check_in_date = Format.parse(check_in_date)
        check_out_date = Format.parse(check_out_date)
        is_cancelled = False
        Validator.checkBoolean(is_cancelled, "is_cancelled")
        total_amount = float(total_amount)
        Validator.checkPositiveFloat(total_amount, "total_amount")
        result = self.Booking_Access.create_booking(check_in_date, check_out_date, is_cancelled, total_amount, guest_id, room_id)
        if result:
            return result


        else:
            return False
    
    def check_user_id_matches_booking_id(self, booking_id, guest_id):
        booking_id = int(booking_id)
        guest_id = int(guest_id)
        Validator.checkID(booking_id)
        Validator.checkID(guest_id)
        hotel_id = self.Booking_Access.check_user_id_matches_booking_id(booking_id, guest_id)
        if not hotel_id:
            return False
        else:
            hotel_id = hotel_id["hotel_id"]
            return hotel_id
        
    def get_bookings_from_guest_id(self, guest_id):
        guest_id = int(guest_id)
        Validator.checkID(guest_id, "guest ID")
        bookings = self.Booking_Access.access_booking_guest(guest_id)
        if bookings:
            return bookings
        else:
            return None

