from views.Menu import Menu
from views.Chart_View import ChartView
from views.RoomType_Menu import RoomType_Menu 
from views.Room_Menu import Room_Menu 
from views.Facility_Menu import Facility_Menu 
import tkinter as tk
from controller.User_Controller import User_Controller
import time
from models.User import User
from datetime import datetime,date
from utils.Formatting import Format
from mythic.mythic_code import Mythic

class UserStoryMenu(Menu):
    def __init__(self, app, prev):
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
        self.add_item("As an admin, I want to analyze my guests",self.dv_2)
        self.add_item("As an admin, I would like to see the revenue per hotel", self.dv_3)
        self.add_item("",self.opt_1)
        self.add_item("",self.opt_1_1)
        self.add_item("",self.opt_1_2)
        self.add_item("",self.opt_2)
        self.add_item("",self.opt_3)
        self.add_item("",self.opt_4)
        self.add_item("back", self.back)
        self._prev_menu = prev
        
    def _authenticate_admin(self):
        """Handles admin authentication."""
        try:
            user_id_input = input("This action requires admin access, please enter your ID: ")
            user_id = int(user_id_input)
        except ValueError:
            print("Invalid ID format. Please enter a number.")
            input("Press Enter to return to the menu.")
            return False
        password = input("Please enter your password: ")
        
        ca = User_Controller()
        rights = ca.check_admin(user_id, password)
        
        if not rights:
            print("Access denied. You are not an admin or your credentials are incorrect.")
            input("Press Enter to return to the menu.")
            return False
        
        print("Admin access granted.")
        return True

    def min_1(self):
        pass
        
    def min_1_1(self):
        """Asks the user for a city and shows all hotels in that city.

        Calls the hotel controller to get hotels and prints their names and star ratings.
        """
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
        """Asks the user for a city and minimum stars, then shows matching hotels.

        Gets hotels from the controller and prints their names and star ratings.
        """
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
        """Asks the user for city, stars, and guests, then shows matching hotels.

        Gets hotels from the controller that match the filters and prints their names and star ratings.
        """
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
        """Asks the user for city, stars, guests, and dates, then shows available hotels.

        Gets hotels from the controller that match all filters and are available in the given date range.
        Prints hotel names and star ratings.

        We added some additional filters like stars and guests, so its more precise to the needs of the customer
        """
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
        """Asks the user for optional filters (city, stars, guests, dates) and shows matching hotels.

        The user can leave any input empty to skip that filter.
        Gets matching hotels from the controller and prints their names and star ratings.
        """
        try:
            city = input("Plesae enter the city in which you are looking for a hotel - if you dant want to filter by city, hit enter:")
            stars = input("How many stars should your hotel at least have - if you dont want to filter by stars, hit enter: ")
            guests = input("How many guests should at least fit into your room - if you dont want to filter by stars, hit enter: ")
            check_in_date = input("When is you check in date - if you dont want to filter by check-in date, hit enter: ")
            check_out_date = input("When is you check out date - if you dont want to filter by check-in-date, hit enter: ")
            hotels = self.app.hotel_Controller.get_selected_filters(city, stars, guests, check_in_date, check_out_date)
        except ValueError as e:
            print(e)
            self.min_1_5()
        print("---------------------")
        if hotels:
            for hotel in hotels:
                print(f"Hotel {hotel.name} has {hotel.stars} stars")
        else:
            print("No hotels match you filters.")
        print("---------------------")
        

    def min_1_6(self):
        """Asks the user for a hotel name and shows detailed information.

        Gets hotel details from the controller and prints name, stars, city, and street.
        """
        hotel_name = input("Please enter the name of the hotel of which you would like to know the details")
        details = self.app.hotel_Controller.get_hotel_details(hotel_name)
        print("---------------------")
        if not details:
            print("Unfortunately no hotel name matches your description")
        else:
            for hotel, street, city in details:
                print(f"Hotel {hotel.name} has {hotel.stars} stars and is located in {city} at {street}")
        print("---------------------")


    
    def min_2(self):
        return self.min_2_2()
    
    def min_2_1(self):
        rooms = self.app.room_Controller.get_rooms()
        counter = 1
        for room in rooms:
            print(f"## {counter} ##")
            print(room.extendedStr())
            counter += 1
    
    def min_2_2(self, fromFunction:bool=False):
        name = input("Please enter the hotel name in which you are looking for a room: ")
        if fromFunction:
            check_in_date = ""
            while check_in_date == "":
                check_in_date = input("When is your check in date: ")
            check_out_date = ""
            while check_out_date == "":
                check_out_date = input("When is your check out date: ")
        else:
            check_in_date = input("When is your check in date - if you dont want to filter by dates, hit enter: ")
            check_out_date = input("When is your check out date - if you dont want to filter by dates, hit enter: ")
        #Check date format
        hotels = self.app.hotel_Controller.get_full_hotel(name, Format().parse(check_in_date), Format().parse(check_out_date))
        rooms = []
        if len(hotels) != 0:
            print("---------------------")
            for hotel in hotels:
                print(hotel)
                for room in hotel.rooms:
                    print(f"{len(rooms) + 1}. {room.extendedStr()}")
                    rooms.append(room)
            print("---------------------")
        else:
            print("---------------------")
            print("No Rooms found")
            print("---------------------")
        if fromFunction and len(hotels) != 0:
            return rooms, Format().parse(check_in_date), Format().parse(check_out_date)


    def min_3(self):
        pass
    
    def min_3_1(self):
        """Adds a new hotel to the database.

        Only works if the user is authenticated as admin.
        Asks for name, stars, and address ID, then tries to add the hotel and shows a success or error message.
        """
        if not self._authenticate_admin():
            return self
        
        name = input("Please name the name of the new hotel: ")
        stars = input("Please type how many stars the hotel has: ")
        address_id = input("Please name the Address-ID of the hotel: ")
        status = self.app.hotel_Controller.add_hotel(name, stars, address_id)
        if status:
            print("Hotel was added successfuly")
        else:
            print("Something went wrong, please try again later")


    def min_3_2(self):
        """Asks the admin to delete a hotel by its ID.

        Only works if the user is authenticated as admin.
        Asks for the hotel ID, then tries to delete it and shows a success or error message.
        """
        if not self._authenticate_admin():
            return self
        
        hotel_id = int(input("Please name the Hotel ID of the hotel you would like to delete"))
        status = self.app.hotel_Controller.delete_hotel(hotel_id)
        if status:
            print("Hotel was delted successfully")
        elif not status:
            print("Unfortunately there is no Hotel with this Hotel ID, so please try again")


    def min_3_3(self):
        """Asks the admin to update hotel information.

        Only works if the user is authenticated as admin.
        Asks for hotel ID and optional new values (name, stars, address ID). 
        Then tries to update the hotel and shows a success or error message.
        """
        if not self._authenticate_admin():
            return self
        
        hotel_id = int(input("Plesae name the Hotel ID of the hotel, of which you'd like to change the information to"))
        name = input("If you'd like to change the name of the hotel please type it in, if you dont want to change the name, hit enter: ")
        stars = input("Please name the new amount of updated stars, if you dont want to change them, press enter: ")
        address_id = input("Please type the new Address ID, if you dont want to change the address, press enter: ")
        status = self.app.hotel_Controller.update_hotel(hotel_id, name, stars, address_id)
        if status:
            print("Hotel information was updated successfully")
        if not status:
            print("There is no hotel with this Hotel ID")
    
    def min_4(self):
        rooms, check_in, check_out = self.min_2_2(fromFunction=True)
        if rooms:
            inputnumber = input("Please enter the choice number")
            # print(rooms[int(inputnumber)-1])
            user = self.login_user()
            booking = self.app.booking_Controller.create_booking(user, rooms[int(inputnumber)-1], check_in, check_out)
            if booking:
                print(f"Success: Booking was created with id {booking.booking_id}")
            else:
                print("unfortunatelly, this did not work, please try again")
        else:
            print("unfortunatelly, this did not work, please try again")    
        return UserStoryMenu(self.app)
    
    def min_5(self):
        """Creates and shows an invoice for a booking.

        Asks the user for a booking ID. If the booking is cancelled, no invoice is created.
        If successful, prints all invoice details. Otherwise, shows an error message.
        """
        booking_id = int(input("Please name the booking ID of which you'd like to create an invoice"))
        result = self.app.invoice_Controller.create_invoice(booking_id)
        if result == "cancelled":
            print("This booking was cancelled, so there is not going to be an invoice")
        elif result:
            hotel, invoice, booking, first_name, last_name, nights = result
            print(f"The invoice was created successfuly, below you can view the invoice:")
            print("---------------------")
            print(f"Invoice ID: {invoice.invoice_id}")
            print(f"Issue Date: {invoice.issue_date}")
            print("---------------------")
            print(f"Guest: {first_name} {last_name}")
            print(f"Hotel: {hotel.name} ({hotel.stars}★)")
            print(f"Check-in: {booking.check_in_date}")
            print(f"Check-out: {booking.check_out_date}")
            print(f"Nights: {nights}")
            print(f"Room ID: {booking.room_id}")
            print("---------------------")
            print(f"Total Amount: {invoice.total_amount:.2f} CHF")
            print("---------------------")
        else:
            print("There was an error genearting the invoice, please try again later")
    
    # Schönere Lösung mit Coach zu besprechen, gefällt mir nicht weil BL in GUI
    def min_6(self):
        user = self.login_user()
        if not user:
            ms = Mythic()
            ms.wtf()
            return UserStoryMenu(self.app)
        bookings = self.app.booking_Controller.get_bookings_from_user(user.guest_id)
        counter = 1
        for booking in bookings:
            print(f"{counter}. : {booking}")
            counter += 1
        choice = input("Which booking would you like to cancel? ")
        state = self.app.booking_Controller.update_booking(bookings[int(choice)-1], "cancel")
        if state:
            print("Booking has been canceled")
            return UserStoryMenu(self.app)
        print("Something went wrong, please open support ticket on localhost:8080/support")
        UserStoryMenu(self.app)
    
    def min_7(self):
        city = input("Please name the city in which you would like to stay")
        check_in_date = input("Please name you desired check-in date")
        check_out_date = input("Please name you desired check-out date")
        print("Thank you, we will now show you all avaiable rooms in this city with their price per night")
        time.sleep(3)
        rooms = self.app.room_Controller.get_available_rooms_city(city, check_in_date, check_out_date)

        for room, price_per_night, name, room_type, nights_high_season, nights_off_season, total_price, average_price_per_night in rooms:
            print(f"{name} | Room ID: {room.room_id} | Type: {room_type}")
            print(f"Base price: {price_per_night:.2f} CHF | High season: {nights_high_season} nights | Off season: {nights_off_season} nights")
            print(f"Total: {total_price:.2f} CHF | Avg. price per night: {average_price_per_night:.2f} CHF")
            print("---------------------")

    
    def min_8(self, fromFunction:bool=False):
        if self._authenticate_admin():
            print("Shorty all bookings will be displayed")
            time.sleep(2)
            bookings = self.app.booking_Controller.get_all_bookings()
            print("---------------------")
            for hotel, booking in bookings:
                if booking.is_cancelled:
                    continue
                else:
                    print(f"Hotel: {hotel.name}, {hotel.stars} stars, ID: {hotel.hotel_id}")
                    print(f"Booking: ID {booking.booking_id}, Guest {booking.guest_id}, Room {booking.room_id}")
                    print(f"Check-in: {booking.check_in_date}, Check-out: {booking.check_out_date}")
                    print(f"Amount: {booking.total_amount:.2f} CHF")
                    print("---------------------")
            print("---------------------")
            if fromFunction:
                return bookings
        else:
            print("You need to be an admin to perform this action")
    
    def min_9(self):
        if self._authenticate_admin():
            rooms = self.app.roomController.get_rooms()
            print("---------------------")
            for room in rooms:
                print(room.extendedStr())
            print("---------------------")
    
    def min_10(self):
        if not self._authenticate_admin():
            ms = Mythic()
            ms.wtf()
            return UserStoryMenu(self.app)
        possibleValues = ["RoomType", "Facilities", "Rooms"]
        counter = 1
        for value in possibleValues:
            print(f"{counter}. {value}")
            counter += 1
        print(f"{counter}. back")
        choice = int(input("pleasy enter your choice"))
        match choice:
            case 1:
                return RoomType_Menu(self.app, self)
            case 2:
                return Facility_Menu(self.app, self)
            case 3:
                return Room_Menu(self.app, self)
            case 4:
                return UserStoryMenu(self.app)
            
    def db_1(self):
        bookings = self.min_8(fromFunction=True)
        counter = 1
        for booking in bookings:
            print(f"{counter}. {booking}")
            counter += 1
        choice = input("Which booking would you like to alter? ")
        booking = bookings[int(choice)-1]
        phonenumber = int(input("Enter altered Phone number"))
        self.app.hotel_Controller.update_booking(phonenumber=phonenumber)
    
    def db_2(self):
        pass
    
    def db_2_1(self):
        def available_rooms(hotel_id):
            check_in_date = input("Please enter your check-in date: ")
            check_out_date = input("Please enter your check-out date: ")
            rooms, nights = self.app.room_Controller.get_available_rooms_by_hotel_id(hotel_id, check_in_date, check_out_date)
            if not rooms:
                print("Unfortunately there are no available rooms during your dates.")
                return UserStoryMenu(self.app)
            else:
                print("The following rooms are available:")
                room_ids = []
                for room, room_type, total_amount in rooms:
                    print(f"Room ID: {room.room_id}, Price per night: {room.price_per_night}, Type: {room_type.description}, Max guests: {room_type.maxGuests}, total amount: {total_amount}")
                    room_ids.append(room.room_id)
                time.sleep(5)
                room_id = input("Please enter the Room ID of the room you'd like to book: ")
            if room_id in room_ids:
                self.app.booking_Controller.create_booking_new()
            else:
                print("Sorry this room does not exist, please try again")

        hotel_name = input("Please enter the name of the hotel you'd like to book with:")
        hotels = self.app.hotel_Controller.get_hotel_details(hotel_name)
        if not hotels:
            print("Unfortunately there is no hotel with this name, please try again")
            return UserStoryMenu(self.app)
        elif len(hotels) > 1:
            print("There are multiple hotels with this name")
            hotel_ids = []
            for hotel, street, city in hotels:
                print(f"hotel ID: {hotel.hotel_id}, street: {street}, city: {city}")
                hotel_ids.append(hotel.hotel_id)
            time.sleep(3)
            hotel_id = int(input("Please now enter the ID of the hotel in which you'd like to make your booking:"))
            if hotel_id in hotel_ids:
                available_rooms(hotel_id)
            else:
                print("Sorry this is not a hotel ID which we showed you, please try again")
                return UserStoryMenu(self.app)
        else:
            hotel = hotels[0][0]
            hotel_id = hotel.hotel_id
            available_rooms(hotel_id)

    
    def db_3(self):
        pass
    
    def db_4(self):
        pass
    
    def db_5(self):
        pass
    
    def db_6(self):
        pass
    
    def dv_1(self):
        if not self._authenticate_admin():
            return self

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
        if not self._authenticate_admin():
            wait = input("Press Enter to return to the menu.")
            return self

        print("\nSelect demographic analysis to display:")
        print("1: Guest Age Distribution")
        print("2: Guest Country Distribution")
        print("3: Guest Booking Frequency (New vs. Returning)")
        choice = input("Enter your choice (1-3): ")

        data = None
        chart_type = None
        data_valid = False

        if choice == '1':
            print("Fetching guest age distribution data...")
            data = self.app.guest_Controller.get_guest_age_distribution_data()
            chart_type = "guest_age_histogram"
            if data and isinstance(data.get('ages'), list) and data['ages']:
                data_valid = True
        elif choice == '2':
            print("Fetching guest country distribution data...")
            data = self.app.guest_Controller.get_guest_country_distribution_data()
            chart_type = "guest_country"
            if data and isinstance(data.get('countries'), list) and data['countries']:
                data_valid = True
        elif choice == '3':
            print("Fetching guest booking frequency data...")
            data = self.app.guest_Controller.get_guest_booking_frequency_data()
            chart_type = "guest_booking_frequency"
            if data and isinstance(data.get('labels'), list) and data['labels'] and \
               isinstance(data.get('sizes'), list) and sum(data['sizes']) > 0:
                data_valid = True
        else:
            print("Invalid choice. Please select a number between 1 and 3.")
            return self

        if data_valid:
            print(f"Displaying {chart_type.replace('_', ' ')} chart in a new window.")
            main_tk_root = tk.Tk()
            main_tk_root.withdraw()
            chart_view = ChartView(self.app, data, chart_type) 
            return chart_view.show_and_wait()
        else:
            print(f"No valid data available to display for {chart_type.replace('_', ' ') if chart_type else 'the selected analysis'}.")
            if data: 
                print(f"Data received but deemed invalid or empty: {data}")
            return self
        
    def dv_3(self):
        results = self.app.chartview_Controller.get_amount_per_hotel()
        ChartView.total_revenue_per_hotel(results)

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

    def back(self):
        return self._prev_menu

    def login_user(self) -> User:
        id = int(input("Please provide user id: "))
        password = input("Please provide password: ")
        return self.app.user_Controller.login_user(id, password)