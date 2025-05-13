import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from views.MenuView import Menu
from controller.Access_Controller import Access_Controller

class HotelMenu(Menu):
    def __init__(self):
        super().__init__("Hotel Menu")
        self.add_item("Search for hotels in a city", self.search_city)
        self.add_item("Search for hotels in a city and with stars", self.search_city_stars)
        self.add_item("Go back", self.back)
        self.ac = Access_Controller()

    def search_city(self):
        city = input("Please name the city, in which you are looking for a hotel:")
        hotels = self.ac.hotel_Access.get_hotel_in_city(city)
        if not hotels:
            print("Unfortunately no hotels match your criteria")
        else:
            for hotel in hotels:
                print(hotel)
        return None

    def search_city_stars(self):
        city = input("Please name the city in which you are looking for a hotel")
        stars = int(input("Please name how many stars your hotel should have"))
        hotels = self.ac.hotel_Access.get_hotel_in_city_stars(city, stars)
        if not hotels:
            print("Unfortunately no hotels match your criteria")
        else:
            for hotel in hotels:
                print(hotel)
        return None

    def back(self):
        return None
