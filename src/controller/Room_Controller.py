from data_Access.Room_Access import Room_Access
from models.Room import Room
from models.RoomType import RoomType
from datetime import date
from datetime import timedelta
from utils.Formatting import Format

class RoomController():
    def __init__(self):
        self.Room_Access = Room_Access()
    
    def get_rooms(self, dateStart: date = None, dateEnd: date = None, hotel_ids: list[int] = None, roomType:RoomType = None)->Room:
        return Room_Access().get_rooms(dateStart=dateStart, dateEnd=dateEnd, hotel_ids=hotel_ids, roomType=roomType)
    
    def get_available_rooms_city(self, city:str, check_in_date:str, check_out_date:str):
        check_in_date = Format.parse(check_in_date)
        check_out_date = Format.parse(check_out_date)
        list = self.Room_Access.get_available_rooms_city(city, check_in_date, check_out_date)
        hotels = []
        for result in list:
            data = dict(result)
            room_id = data["room_id"]
            room_no = data["room_number"]
            price_per_night = data["price_per_night"]
            room = Room(room_id, room_no, price_per_night)
            name = data["name"]
            room_type = data["room_type"]

            nights_high_season = 0
            current = check_in_date
            while current < check_out_date:
                if 5 <= current.month <= 9:
                    nights_high_season += 1
                current += timedelta(days=1)
            nights_offseason = (check_out_date - check_in_date).days - nights_high_season
            total_price = nights_high_season * price_per_night * 1.2 + nights_offseason * price_per_night * 0.8
            average_price_per_night = total_price/(nights_high_season+nights_offseason)
            hotels.append((room, price_per_night, name, room_type, nights_high_season, nights_offseason, total_price, average_price_per_night))
        return hotels

