from data_Access.Room_Access import Room_Access
from models.Room import Room
from models.RoomType import RoomType
from datetime import date

class RoomController():
    def __init__(self):
        pass
    
    def get_rooms(self, dateStart: date = None, dateEnd: date = None, hotel_ids: list[int] = None, roomType:RoomType = None)->Room:
        return Room_Access().get_rooms(dateStart=dateStart, dateEnd=dateEnd, hotel_ids=hotel_ids, roomType=roomType)