import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.Validator import Validator
from models.Facility import Facility
from models.RoomType import RoomType

class Room:
    def __init__(self, room_id: int, room_no: str, price_per_night: float, facilities:list[Facility] = [], roomType:RoomType = None, hotelid:int=None):
        self.validator = Validator()
        self.validator.checkID(room_id)
        self.validator.checkStr(room_no, "room_no")
        self.validator.checkPositiveFloat(price_per_night, "price_per_night")
        self.room_id = room_id
        self.room_no = room_no
        self.price_per_night = price_per_night
        self.facilities = facilities
        self.roomType = roomType
        self.hotelid = hotelid
    """
    @property
    def room_id(self):
        return self.room_id

    @room_id.setter
    def room_id(self, room_id):
        self.validator.checkID(room_id)
        self.room_id = room_id

    @property
    def room_no(self):
        return self.room_no

    @room_no.setter
    def room_no(self, room_no):
        self.validator.checkStr(room_no, "room_no")
        self.room_no = room_no

    @property
    def price_per_night(self):
        return self.price_per_night

    @price_per_night.setter
    def price_per_night(self, price_per_night):
        self.validator.checkPositiveFloat(price_per_night, "price_per_night")
        self.price_per_night = price_per_night
    """
    

    def __str__(self):
        return f"Room {self.room_no} costs {self.price_per_night} per night and has room ID: {self.room_id}"

    def to_dict(self):
        return{
            "room_id": self.room_id,
            "room_no": self.room_no,
            "price_per_night": self.price_per_night
        }