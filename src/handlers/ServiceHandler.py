import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.BookingService import BookingService
from services.UserService import UserService
from services.RoomTypeService import RoomTypeServie
from services.RoomService import RoomService
from services.InvoiceService import Invoiceservice
from services.HotelService import Hotelservice

class ServiceHandler:
    def __init__(self):
        self.booking_service = BookingService()
        self.user_service = UserService()
        self.room_type_service = RoomTypeServie()
        self.room_service = RoomService()
        self.invoice_service = Invoiceservice()
        self.hotel_service = Hotelservice()