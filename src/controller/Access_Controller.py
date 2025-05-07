import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data_Access.Booking_Access import Booking_Access
from data_Access.User_Access import User_Access
from data_Access.RoomType_Access import RoomTypeServie
from data_Access.Room_Access import Room_Access
from data_Access.Invoice_Access import Invoice_Access
from data_Access.Hotel_Access import Hotel_Access

class Access_Controller:
    def __init__(self):
        self.booking_Access = Booking_Access()
        self.user_Access = User_Access()
        self.room_type_Access = RoomTypeServie()
        self.room_Access = Room_Access()
        self.invoice_Access = Invoice_Access()
        self.hotel_Access = Hotel_Access()