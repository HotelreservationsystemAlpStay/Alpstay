from views.Menu import Menu
from views.Chart_View import ChartView 
import tkinter as tk

class UserStoryMenu(Menu):
    def __init__(self, app):
        super().__init__("UserStories", app)
        self.add_item("As a guest, I want to search for a hotel in a city, so that i can choose the one, that meets my criteria",self.min_1)
        self.add_item("Criteria 1: City",self.min_1_1)
        self.add_item("Criteria 2: Stars",self.min_1_2)
        self.add_item("Criteria 3: Amount of guests in a room",self.min_1_3)
        self.add_item("Criteria 4: Availability (Room in a hotel is available between start date and end date)",self.min_1_4)
        self.add_item("Criteria 5: Combine the upper four criteria",self.min_1_5)
        self.add_item("Criteria 6: The following Information should be displayed: Hotel name, hotel address, amount of stars",self.min_1_6)
        self.add_item("As a guest, I want to see the details of different room types, which are available in a hotel, including the following information for this room: maximum amount of guests, description, price and facilities",self.min_2)
        self.add_item("As a guest, I want to see the following information for each room: room type, maximum amount of guest, description, facilities, price per night and total price",self.min_2_1)
        self.add_item("As a guest, I only want to see available rooms if I have specified the dates of my stay",self.min_2_2)
        self.add_item("As an admin, I want to have the possibility to update information about hotels",self.min_3)
        self.add_item("As an admin, I want to add new hotels to the system",self.min_3_1)
        self.add_item("As an admin, I want to delete hotels from the system",self.min_3_2)
        self.add_item("As an admin, I want to update information of hotel",self.min_3_3)
        self.add_item("As a guest, I want to book a room in a certain hotel",self.min_4)
        self.add_item("As a guest, I want to receive an invoice after my stay",self.min_5)
        self.add_item("As a guest, I want to be able to cancel my booking",self.min_6)
        self.add_item("As a guest, I want to have dynamics prices to profit from dynamic pricing",self.min_7)
        self.add_item("As an admin, I want to see all bookings",self.min_8)
        self.add_item("As an admin, I want to see all rooms with their facilities",self.min_9)
        self.add_item("As an admin, I want to be capable to update master data (RoomTypes, Facilities, Prices)",self.min_10)
        self.add_item("As an admin, I want to update missing information in bookings",self.db_1)
        self.add_item("As a guest, I want to see my booking history",self.db_2)
        self.add_item("For all bookings, I should be able to use the following action 'create', 'update', 'cancel'",self.db_2_1)
        self.add_item("As a guest, I want to create a rating about the stay at a hotel",self.db_3)
        self.add_item("As a guest, I want to read ratings before I book",self.db_4)
        self.add_item("",self.db_5)
        self.add_item("",self.db_6)
        self.add_item("As an admin, I want to see the occupancy rate for each room type",self.dv_1)
        self.add_item("As an admin, I want to analyze my guests based on demografic attributes",self.dv_2)
        self.add_item("",self.opt_1)
        self.add_item("",self.opt_1_1)
        self.add_item("",self.opt_1_2)
        self.add_item("",self.opt_2)
        self.add_item("",self.opt_3)
        self.add_item("",self.opt_4)
        
    def min_1(self):
        pass
        
    def min_1_1(self):
        city = input("Please enter the city you want to search for: ")
        hotels = self.app.hotel_Controller.get_hotel_in_city(city)
        print("---------------------")
        if hotels:
            for hotel in hotels:
                print(f"Hotel {hotel.name} has {hotel.stars} stars")
        else:
            print("No hotels found in the specified city.")
        print("---------------------")
    def min_1_2(self):
        city = input("Please enter the city in which you are looking for a hotel")
        stars = int(input("How many stars should your hotel at least have?"))
        hotels = self.app.hotel_Controller.get_hotel_in_city_stars(city, stars)
        print("---------------------")
        if hotels:
            for hotel in hotels:
                print(f"Hotel {hotel.name} has {hotel.stars} stars")
        else:
            print("No hotels match you filters.")
            print("---------------------")
    
    def min_1_3(self):
        city = input("Please enter the city in which you are looking for a hotel")
        stars = int(input("How many stars should your hotel at least have?"))
        guests = int(input("How many guests should at least fit into your room"))
        hotels = self.app.hotel_Controller.get_hotel_in_city_stars_guests(city, stars, guests)
        print("---------------------")
        if hotels:
            for hotel in hotels:
                print(f"Hotel {hotel.name} has {hotel.stars} stars")
        else:
            print("No hotels match you filters.")
        print("---------------------")
    
    def min_1_4(self):
        city = input("Please enter the city in which you are looking for a hotel: ")
        stars = int(input("How many stars should your hotel at least have: "))
        guests = int(input("How many guests should at least fit into your room: "))
        check_in_date = input("When is you check in date: ")
        check_out_date = input("When is you check out date: ")
        hotels = self.app.hotel_Controller.get_hotel_in_city_booking(city, stars, guests, check_in_date, check_out_date)
        print("---------------------")
        if hotels:
            for hotel in hotels:
                print(f"Hotel {hotel.name} has {hotel.stars} stars")
        else:
            print("No hotels match you filters.")
        print("---------------------")
        
    def min_1_5(self):
        city = input("Plesae enter the city in which you are looking for a hotel - if you dant want to filter by city, hit enter:")
        stars = input("How many stars should your hotel at least have - if you dont want to filter by stars, hit enter: ")
        guests = input("How many guests should at least fit into your room - if you dont want to filter by stars, hit enter: ")
        check_in_date = input("When is you check in date - if you dont want to filter by stars, hit enter: ")
        check_out_date = input("When is you check out date - if you dont want to filter by stars, hit enter: ")
        hotels = self.app.hotel_Controller.get_selected_filters(city, stars, guests, check_in_date, check_out_date)
        print("---------------------")
        if hotels:
            for hotel in hotels:
                print(f"Hotel {hotel.name} has {hotel.stars} stars")
        else:
            print("No hotels match you filters.")
        print("---------------------")
        

    def min_1_6(self):
        pass
    
    def min_2(self):
        pass
    
    def min_2_1(self):
        rooms = self.app.room_Controller.get_rooms()
        counter = 1
        for room in rooms:
            print(f"## {counter} ##")
            print(room)
            counter += 1
    
    def min_2_2(self):
        pass
    
    def min_3(self):
        pass
    
    def min_3_1(self):
        pass
    
    def min_3_2(self):
        pass
    
    def min_3_3(self):
        pass
    
    def min_4(self):
        pass
    
    def min_5(self):
        pass
    
    def min_6(self):
        pass
    
    def min_7(self):
        pass
    
    def min_8(self):
        pass
    
    def min_9(self):
        pass
    
    def min_10(self):
        pass
    
    def db_1(self):
        pass
    
    def db_2(self):
        pass
    
    def db_2_1(self):
        pass
    
    def db_3(self):
        pass
    
    def db_4(self):
        pass
    
    def db_5(self):
        pass
    
    def db_6(self):
        pass
    
    def dv_1(self):
        print("Fetching room occupancy data...")

        main_tk_root = tk.Tk()
        main_tk_root.withdraw()
        occupancy_data = self.app.roomType_Controller.get_room_occupancy_data()
        if occupancy_data and occupancy_data.get('room_type') and occupancy_data.get('count'):
            print("Displaying occupancy chart in a new window")
            chart = ChartView(self.app, occupancy_data, "occupancy")
            return chart.show_and_wait() 
        else:
            print("No occupancy data available to display.")
            if occupancy_data:
                print(f"Data received: {occupancy_data}")
            return self
    
    def dv_2(self):
       pass
    
    def opt_1(self):
        pass
    
    def opt_1_1(self):
        pass
    
    def opt_1_2(self):
        pass
    
    def opt_2(self):
        pass
    
    def opt_3(self):
        pass
    
    def opt_4(self):
        pass
