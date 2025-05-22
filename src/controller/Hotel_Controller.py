import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.Validator import Validator
from data_Access.Hotel_Access import Hotel_Access
from models.Hotels import Hotel
from controller.User_Controller import User_Controller
from utils.Formatting import Format

class Hotel_Controller:
    def __init__(self):
        self.hotel_access = Hotel_Access()
    
    def get_hotel_in_city(self, city):
        Validator.checkStr(city, "city")
        result = self.hotel_access.access_hotel_in_city(city)
        hotels = []
        for row in result:
            data = dict(row)
            hotel = Hotel(
                hotel_id=data["hotel_id"],
                name=data["name"],
                stars=data["stars"]
            )
            hotels.append(hotel)
        return hotels
    
    def get_hotel_in_city_stars(self, city, min_stars):
        Validator.checkStr(city, "city")
        Validator.checkStars(min_stars)
        result = self.hotel_access.access_hotel_in_city_stars(city, min_stars)
        hotels = []
        for row in result:
            data = dict(row)
            hotel = Hotel(
                hotel_id=data["hotel_id"],
                name=data["name"],
                stars=data["stars"]
            )
            hotels.append(hotel)
        return hotels
    
    def get_hotel_in_city_stars_guests(self, city, min_stars, guests):
        Validator.checkStr(city, "city")
        Validator.checkStars(min_stars)
        Validator.checkPositiveInteger(guests, "Guests")
        result = self.hotel_access.access_hotel_in_city_stars_guests(city, min_stars, guests)
        hotels = []
        for row in result:
            data = dict(row)
            hotel = Hotel(
                hotel_id=data["hotel_id"],
                name=data["name"],
                stars=data["stars"]
            )
            hotels.append(hotel)
        return hotels
    
    def get_hotel_in_city_booking(self, city, min_stars, guests, check_in_date, check_out_date):
        check_in_date = Format().parse(check_in_date)
        check_out_date = Format().parse(check_out_date)
        Validator.checkStr(city, "city")
        Validator.checkStars(min_stars)
        Validator.checkPositiveInteger(guests, "Guests")
        Validator.checkDate(check_in_date, "Check-in date")
        Validator.checkDate(check_out_date, "Check-out date")
        Validator.checkDateDifference(check_in_date, check_out_date)

        result = self.hotel_access.access_hotel_in_city_booking(
            city, min_stars, guests, check_in_date, check_out_date
        )
        hotels = []
        for row in result:
            data = dict(row)
            hotel = Hotel(
                hotel_id=data["hotel_id"],
                name=data["name"],
                stars=data["stars"]
            )
            hotels.append(hotel)
        return hotels
    
    def get_selected_filters(self, city, min_stars, guests, check_in_date, check_out_date):
        if city:
            Validator.checkStr(city, "city")
        if min_stars:
            min_stars = int(min_stars)
            Validator.checkStars(min_stars)
        if guests:
            guests = int(guests)
            Validator.checkPositiveInteger(guests, "Guests")
        if (not check_in_date and check_out_date) or (check_in_date and not check_out_date):
            raise ValueError("If you provide a check-in-date, you must provide a check-out-date and the other way around")  
        elif check_in_date and check_out_date:
            check_in_date = Format().parse(check_in_date)
            check_out_date = Format().parse(check_out_date)
            Validator.checkDate(check_in_date, "Check-in date")
            Validator.checkDate(check_out_date, "Check-out date")
            Validator.checkDateDifference(check_in_date, check_out_date)
        result = self.hotel_access.access_selected_filters(city, min_stars, guests, check_in_date, check_out_date)
        hotels = []
        for row in result:
            data = dict(row)
            hotel = Hotel(
                hotel_id=data["hotel_id"],
                name=data["name"],
                stars=data["stars"]
            )
            hotels.append(hotel)
        return hotels
    
    def get_hotel_details(self, hotel_name):
        result = self.hotel_access.access_hotel_details(hotel_name)
        if not result:
            return []
        hotels = []
        for row in result: 
            data = dict(row)
            hotel = Hotel(
                hotel_id=data["hotel_id"],
                name=data["name"],
                stars=data["stars"]
            )
            street = data["street"]
            city = data["city"]
            hotels.append((hotel, street, city))
        return hotels
    
    def add_hotel(self, name, stars, address_id):
        status = self.hotel_access.access_add_hotel(name, stars, address_id)
        return status

    def delete_hotel(self, hotel_id):
        status = self.hotel_access.access_delete_hotel(hotel_id)
        return status
    
    def update_hotel(self, hotel_id, name, stars, address_id):
        if not name and not stars and not address_id:
            raise ValueError("You must change at least one information")
        if stars:
            stars = int(stars)
        if address_id:
            address_id = int(address_id)
        return self.hotel_access.access_update_hotel(hotel_id, name, stars, address_id)