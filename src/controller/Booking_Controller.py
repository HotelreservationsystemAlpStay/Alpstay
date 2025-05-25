from models.User import User
from models.Room import Room
from models.Booking import Booking
from datetime import datetime
from data_Access.Booking_Access import Booking_Access

class Booking_Controller:
    def __init__(self):
        pass
    
    def create_booking(self, user:User, room:Room, startDate:datetime, endDate:datetime):
        booking = Booking_Access().create_booking(check_in_date=startDate, check_out_date=endDate, is_cancelled=False, total_amount=1, guest_id=user.guest_id, room_id=room.room_id)
        if booking:
            return booking
        return None
    
    def update_booking(selfuser:User, booking:Booking):
        pass