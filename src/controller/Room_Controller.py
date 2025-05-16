from data_Access.Room_Access import Room_Access
from datetime import date
from models.Room import Room
from models.RoomType import RoomType

class RoomController:
    def __init__(self):
        pass

    def get_rooms(self, dateStart: date = None, dateEnd: date = None, hotel_ids: list[int] = None, roomType:RoomType = None):
        return Room_Access().get_rooms(dateStart, dateEnd, hotel_ids, roomType)