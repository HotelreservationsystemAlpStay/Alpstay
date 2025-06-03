from views.Menu import Menu
from controller.Access_Controller import Access_Controller
from datetime import date
from utils.Formatting import Format
from views.Room_Menu import Room_Menu

class HotelMenu(Menu):
    def __init__(self, app):
        super().__init__("Hotel Menu", app)
        self.add_item("Search for hotels in a city", self.search_city)
        self.add_item("Search for hotels in a city and with stars", self.search_city_stars)
        self.add_item("Search for hotels in a city, with stars and your amount of guests", self.search_city_stars_guests)
        self.add_item("Search for hotels in a city, with stars, your amount of guests and your booking dates", self.search_city_stars_guests_dates)
        self.add_item("Search with your own filters", self.get_optional_filters)
        self.add_item("I wanna get the details to a specific hotel", self.hotel_details)
        self.add_item("I want to add a hotel (Must be an admin)", self.add_hotel)
        self.add_item("I want do delete a hotel (Must be an admin)", self.delete_hotel)
        self.add_item("I want to update hotel informations (Must be an admin)", self.update_hotel)
        self.add_item("I want to see rooms from hotel, which satisfy my needs", self.search_hotel_room)
        self.add_item("Go back", self.back)

    def search_city(self):
        city = input("Please name the city, in which you are looking for a hotel: ")
        hotels = self.app.hotel_Controller.get_hotel_in_city(city)
        if not hotels:
            print("Unfortunately no hotels match your criteria")
        else:
            for hotel in hotels:
                print(f"{hotel.name} has {hotel.stars} stars and is located in {city}")
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
    
    def search_city_stars_guests(self):
        city = input("Please name the city in which you are looking for a hotel")
        stars = int(input("Please name how many stars your hotel should have"))
        guests = int(input("Please name how many guests are staying in your room"))
        hotels = self.ac.hotel_Access.get_hotel_in_city_stars_guests(city, stars, guests)
        if not hotels:
            print("Unfortunately no hotels match your criteria")
        else:
            for hotel in hotels:
                print(hotel)
        return None
    
    def search_city_stars_guests_dates(self):
        city = input("Please name the city in which you are looking for a hotel")
        stars = int(input("Please name how many stars your hotel should have"))
        guests = int(input("Please name how many guests are staying in your room"))
        check_in_date = input("Please name your check-in date")
        check_out_date = input("Please name your check-out date")
        check_in_date_formatted = Format.parse(check_in_date)
        check_out_date_formatted = Format.parse(check_out_date)
        
        hotels = self.ac.hotel_Access.get_hotel_in_city_booking(city, stars, guests, check_in_date_formatted, check_out_date_formatted)
        if not hotels:
            print("Unfortunately no hotels match your criteria")
        else:
            for hotel in hotels:
                print(hotel)
        return None
    
    def get_optional_filters(self):
        notusable = input("All the following filters are optional, if you dont want to you use, just hit enter, confirm this by hitting enter right now")
        city = input("Please name the city in which you are looking for a hotel: ")
        if not city:
            city = "all"
        stars = input("Please name how many stars your hotel should have: ")
        if not stars:
            stars = "all"
        else:
            stars = int(stars)
        guests = input("Please name how many guests are staying in your room: ")
        if not guests:
            guests = "all"
        else:
            guests = int(guests)
        check_in_date = input("Please name your check-in date: ")
        if not check_in_date:
            check_in_date = "all"
        check_out_date = input("Please name your check-out date: ")
        if not check_out_date:
            check_out_date = "all"
        if check_in_date != "all" and check_out_date != "all":
            check_in_date_formatted = Format.parse(check_in_date)
            check_out_date_formatted = Format.parse(check_out_date)
        hotels = self.ac.hotel_Access.get_selected_filters(city, stars, guests, check_in_date, check_out_date)
        if not hotels:
            print("Unfortunately no hotels match your criteria")
        else:
            for hotel in hotels:
                print(hotel)
        return None
    
    def hotel_details(self):
        name = input("Please write the name of your hotel").strip() #Unnötigte Leerzeichen entfernen
        hotels = self.ac.hotel_Access.get_hotel_details(name)
        if not hotels:
            print("Unfortunately no hotels match your criteria")
        else: 
            for hotel in hotels:
                print(hotel)
    def add_hotel(self):
        user_id = int(input("Please name your user ID"))
        password = input("Please name your password")
        name = input("Please type in the name of the hotel")
        stars = int(input("Please type in how many stars the hotel has"))
        address_id = int(input("Please type in the address_id of the hotel"))
        status = self.ac.hotel_Access.add_hotel(user_id, password, name, stars, address_id)
        if status:
            print(f"Hotel {name} has been successfully created")

    def delete_hotel(self):
        user_id = int(input("Please name your user ID"))
        password = input("Please name your password")
        hotel_id = int(input("Please name the hotel ID of the hotel you'd like to delete"))
        status = self.ac.hotel_Access.delete_hotel(user_id, password, hotel_id)
        if status:
            print(f"The hotel with the hotel_id {hotel_id} was successfully deleted")
        else:
            print("There is no hotel with this hotel ID")
    
    def update_hotel(self):
        user_id = int(input("Please name your user ID"))
        password = input("Please name your password")
        hotel_id = input("Please name the hotel ID of the hotel you'd like to change the information to")
        if not hotel_id:
            hotel_id = None
        else:
            hotel_id = int(hotel_id)
        name = input("Please type in the new name of the hotel, if you'd like to change the name, else just press enter")
        if not name:
            name = None
        stars = input("Please type in the new amount of stars of the hotel, if you'd like to change the hotel, else just press enter")
        if not stars:
            stars = None
        else:
            stars = int(stars)
        address_id = input("Please type in the new address ID of the hotel, if you'd like to change it, else just press enter")
        if not address_id:
            address_id = None
        else:
            address_id = int(address_id)
        status = self.ac.hotel_Access.update_hotel(user_id, password, hotel_id, name, stars, address_id)
        if status:
            print("Hotel information updated successfully")
        else:
            print("No hotel with this hotel ID found")
    #get_available rooms mues na gmacht werde
    
    def search_hotel_room(self):
        pass

    def back(self):
        return None
    
