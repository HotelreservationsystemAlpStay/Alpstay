import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from views.Menu import Menu
from models.Hotels import Hotel
from models.Room import Room
from controller.Room_Controller import RoomController

class Room_Menu(Menu):
    def __init__(self, app, hotels:list[Hotel]=None):
        super().__init__(title="Room Menu", app=app)
        self.hotels = hotels
        self.add_item("Rooms for provided hotels", self.get_rooms)
        if not hotels:
            pass
        elif len(hotels) == 1:
            pass
        else:
            pass

    def get_rooms(self):
        print(self.hotels)
        hotel_ids = []
        for hotel in self.hotels:
            hotel_ids.append(hotel.hotel_id)
        result = self.app.room_controller.get_rooms(hotel_ids=hotel_ids)
        for item in result:
            print(item)