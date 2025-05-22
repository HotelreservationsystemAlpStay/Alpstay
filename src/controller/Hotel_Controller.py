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
        output = []
        for hotel in hotels:
            output.append(f"{hotel.name} in {city} has {hotel.stars} stars")
        return output
    
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
        output = []
        for hotel in hotels:
            output.append(f"{hotel.name} in {city} has {hotel.stars} stars")
        return output
    
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
        output = []
        for hotel in hotels:
            output.append(f"{hotel.name} in {city} has {hotel.stars} stars")
        return output
    
    def get_selected_filters(self, city, min_stars, guests, check_in_date, check_out_date):
        check_in_date = Format().parse(check_in_date)
        check_out_date = Format().parse(check_out_date)
        if city != "all":
            Validator.checkStr(city, "city")
        if min_stars != "all":
            Validator.checkStars(min_stars)
        if guests != "all":
            Validator.checkPositiveInteger(guests, "Guests")
        if (check_in_date != "all" and check_out_date == "all") or (check_in_date == "all" and check_out_date != "all"):
            raise ValueError("If you provide a check-in-date, you must provide a check-out-date and the other way around")  
        elif check_in_date != "all" and check_out_date != "all":
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
            hotels.append((hotel, data["city"], data["street"]))
        output = []
        for hotel, city, street in hotels:
            output.append(f"{hotel.name} has {hotel.stars} stars, is located in {city} at: {street}")
        return output
    
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
        output = []
        for hotel, street, city in hotels: 
            output.append(f"The hotel {hotel.name} you mentioned has {hotel.stars} stars and is located in {city} at {street}")
        return output
    
    def add_hotel(self, user_id, password, name, stars, address_id):
        uh = User_Controller()
        if uh.check_admin(user_id, password) != True:
            raise ValueError("You need admin rights to perform this action")
        return self.hotel_access.access_add_hotel(name, stars, address_id)

    def delete_hotel(self, user_id, password, hotel_id):
        uh = User_Controller()
        if uh.check_admin(user_id, password) != True:
            raise ValueError("You need admin rights to perform this action")

        result = self.hotel_access.access_delete_hotel(hotel_id)
        return result
    
    def update_hotel(self, user_id, password, hotel_id, name, stars, address_id):
        uh = User_Controller()
        if uh.check_admin(user_id, password) != True:
            raise ValueError("You need admin rights to perform this action")
        if not hotel_id:
            raise ValueError("You must provide the hotel ID of the hotel you would like to change")
        if name is None and stars is None and address_id is None:
            raise ValueError("You must change at least one information of the hotel")
        return self.hotel_access.access_update_hotel(hotel_id, name, stars, address_id)







            

hotels = Hotel_Controller()
hotels = hotels.get_hotel_in_city("Zürich")
for hotel in hotels:
    print(hotel)