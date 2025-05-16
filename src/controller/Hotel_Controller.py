import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data_Access.Hotel_Access import Hotel_Access

class Hotel_Controller:
    def __init__(self):
        self.query = """
        SELECT DISTINCT hotel_id, name, stars, city, street
        FROM extended_hotel_room_booking
        WHERE 1=1
        """
        self.WHERE_CITY = "WHERE city = ?"
        self.WHERE_STAR = ""

    def get_information(self):
        return "Hello"
    
    def get_hotels(self, city=None, stars=None):
        return Hotel_Access().get_hotel_in_city(city=city)