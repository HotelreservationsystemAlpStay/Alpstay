from views.Menu import Menu
from views.Chart_View import ChartView
from views.Room_Type_Menu import Room_Type_Menu 
from views.Room_Menu import Room_Menu 
from views.Facility_Menu import Facility_Menu 
import tkinter as tk
from managers.User_Manager import User_Manager
import time
from models.User import User
from datetime import datetime,date
from utils.Formatting import Format
from mythic.mythic_code import Mythic

class UserStoryMenu(Menu):
    def __init__(self, app, prev):
        super().__init__("UserStories", app)
        self.add_item("(Min 1) As a guest, I want to search for a hotel in a city, so that i can choose the one, that meets my criteria",self.min_1)
        self.add_item("(Min 1.1) Criteria 1: City",self.min_1_1)
        self.add_item("(Min 1.2) Criteria 2: Stars",self.min_1_2)
        self.add_item("(Min 1.3) Criteria 3: Amount of guests in a room",self.min_1_3)
        self.add_item("(Min 1.4) Criteria 4: Availability (Room in a hotel is available between start date and end date)",self.min_1_4)
        self.add_item("(Min 1.5) Criteria 5: Combine the upper four criteria",self.min_1_5)
        self.add_item("(Min 1.6) Criteria 6: The following Information should be displayed: Hotel name, hotel address, amount of stars",self.min_1_6)
        self.add_item("(Min 2) As a guest, I want to see the details of different room types, which are available in a hotel, including the following information for this room: maximum amount of guests, description, price and facilities",self.min_2)
        self.add_item("(Min 2.1) As a guest, I want to see the following information for each room: room type, maximum amount of guest, description, facilities, price per night and total price",self.min_2_1)
        self.add_item("(Min 2.2) As a guest, I only want to see available rooms if I have specified the dates of my stay",self.min_2_2)
        self.add_item("(Min 3) As an admin, I want to have the possibility to update information about hotels",self.min_3)
        self.add_item("(Min 3.1) As an admin, I want to add new hotels to the system",self.min_3_1)
        self.add_item("(Min 3.2) As an admin, I want to delete hotels from the system",self.min_3_2)
        self.add_item("(Min 3.3) As an admin, I want to update information of hotel",self.min_3_3)
        self.add_item("(Min 4) As a guest, I want to book a room in a certain hotel",self.min_4)
        self.add_item("(Min 5) As a guest, I want to receive an invoice after my stay",self.min_5)
        self.add_item("(Min 6) As a guest, I want to be able to cancel my booking",self.min_6)
        self.add_item("(Min 7) As a guest, I want to have dynamics prices to profit from dynamic pricing",self.min_7)
        self.add_item("(Min 8) As an admin, I want to see all bookings",self.min_8)
        self.add_item("(Min 9) As an admin, I want to see all rooms with their facilities",self.min_9)
        self.add_item("(Min 10)As an admin, I want to be capable to update master data (RoomTypes, Facilities, Prices)",self.min_10)
        self.add_item("(DB 1) As an admin, I want to update missing information in bookings",self.db_1)
        self.add_item("(DB 2) As a guest, I want to see my booking history",self.db_2)
        self.add_item("(DB 2.1) I want to create a new booking",self.db_2_1_1)
        self.add_item("(DB 3) As a guest, I want to create a rating about the stay at a hotel",self.db_3)
        self.add_item("(DB 4) As a guest, I want to read ratings before I book",self.db_4)
        self.add_item("(DB 5)",self.db_5)
        self.add_item("(DB 6)",self.db_6)
        self.add_item("(DV 1) As an admin, I want to see the occupancy rate for each room type",self.dv_1)
        self.add_item("(DV 2) As an admin, I want to analyze my guests",self.dv_2)
        self.add_item("(DV 3) As an admin, I would like to see the revenue per hotel", self.dv_3)
        self.add_item("(Opt 1) with 1.1 and 1.2",self.opt_1)
        self.add_item("(Opt 2)",self.opt_2)
        self.add_item("(Opt 3)",self.opt_3)
        self.add_item("(Opt 4)",self.opt_4)
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
        
        ca = User_Manager()
        try:
            rights = ca.check_admin(user_id, password)
        except ValueError as e:
            print(e)
            return False
        
        if not rights:
            print("Access denied. You are not an admin or your credentials are incorrect.")
            input("Press Enter to return to the menu.")
            return False
        
        print("Admin access granted.")
        return True
    
    def _authentice_guest(self):
        #try user id 1 with this password fciwke-peOlme-8rutjj
        try:
            user_id_input = input("This action requires you to be logged in, please enter your ID: ")
            user_id = int(user_id_input)
        except ValueError:
            print("Invalid ID format. Please enter a number.")
            input("Press Enter to return to the menu.")
            return False
        password = input("Please enter your password: ")
        
        ca = User_Manager()
        try:
            rights = ca.login_user(user_id, password)
        except ValueError as e:
            print(e)
            return False
        if rights:
            return user_id
        else:
            return False
        
    def _not_implemented_yet(self):
        """Prints a message indicating that the feature is not implemented and waits for user input."""
        print("The logic for this user story has not been implemented yet.")
        input("Press Enter to return to the menu.")

    def min_1(self):
        print("Welcome to the hotel search system! Please choose from min_1.1 to min_1.6 to search for hotels based on your criteria.")
        print("----------------------")
        
    def min_1_1(self):
        """Asks the user for a city and shows all hotels in that city.

        Calls the hotel Manager to get hotels and prints their names and star ratings.
        """
        city = input("Please enter the city you want to search for: ")
        try:
            hotels = self.app.hotel_Manager.get_hotel_in_city(city)
        except ValueError as e:
            print(e)
            hotels = []
        print("---------------------")
        if hotels:
            for hotel in hotels:
                print(f"Hotel {hotel.name} has {hotel.stars} stars")
        else:
            print("No hotels found in the specified city.")
        print("---------------------")
    def min_1_2(self):
        """Asks the user for a city and minimum stars, then shows matching hotels.

        Gets hotels from the Manager and prints their names and star ratings.
        """
        city = input("Please enter the city in which you are looking for a hotel: ")
        try:
            stars = int(input("How many stars should your hotel at least have? "))
            hotels = self.app.hotel_Manager.get_hotel_in_city_stars(city, stars)
        except ValueError as e:
            print(e)
            hotels = []
        print("---------------------")
        if hotels:
            for hotel in hotels:
                print(f"Hotel {hotel.name} has {hotel.stars} stars")
        else:
            print("No hotels match you filters.")
            print("---------------------")
    
    def min_1_3(self):
        """Asks the user for city, stars, and guests, then shows matching hotels.

        Gets hotels from the Manager that match the filters and prints their names and star ratings.
        """
        city = input("Please enter the city in which you are looking for a hotel: ")
        try:
            stars = int(input("How many stars should your hotel at least have? "))
            guests = int(input("How many guests should at least fit into your room "))
            hotels = self.app.hotel_Manager.get_hotel_in_city_stars_guests(city, stars, guests)
        except ValueError as e:
            print(e)
            hotels = []
        print("---------------------")
        if hotels:
            for hotel in hotels:
                print(f"Hotel {hotel.name} has {hotel.stars} stars")
        else:
            print("No hotels match you filters.")
        print("---------------------")
    
    def min_1_4(self):
        """Asks the user for city, stars, guests, and dates, then shows available hotels.

        Gets hotels from the Manager that match all filters and are available in the given date range.
        Prints hotel names and star ratings.

        We added some additional filters like stars and guests, so its more precise to the needs of the customer
        """
        city = input("Please enter the city in which you are looking for a hotel: ")
        try:
            stars = int(input("How many stars should your hotel at least have: "))
            guests = int(input("How many guests should at least fit into your room: "))
            check_in_date = input("When is you check in date: ")
            check_out_date = input("When is you check out date: ")
            hotels = self.app.hotel_Manager.get_hotel_in_city_booking(city, stars, guests, check_in_date, check_out_date)
        except ValueError as e:
            print(e)
            hotels = []
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
        Gets matching hotels from the Manager and prints their names and star ratings.
        """
        try:
            city = input("Plesae enter the city in which you are looking for a hotel - if you dant want to filter by city, hit enter:")
            stars = input("How many stars should your hotel at least have - if you dont want to filter by stars, hit enter: ")
            guests = input("How many guests should at least fit into your room - if you dont want to filter by stars, hit enter: ")
            check_in_date = input("When is you check in date - if you dont want to filter by check-in date, hit enter: ")
            check_out_date = input("When is you check out date - if you dont want to filter by check-in-date, hit enter: ")
            hotels = self.app.hotel_Manager.get_selected_filters(city, stars, guests, check_in_date, check_out_date)
        except ValueError as e:
            print(e)
            hotels = []
        print("---------------------")
        if hotels:
            for hotel in hotels:
                print(f"Hotel {hotel.name} has {hotel.stars} stars")
        else:
            print("No hotels match you filters.")
        print("---------------------")
        

    def min_1_6(self):
        """Asks the user for a hotel name and shows detailed information.

        Gets hotel details from the Manager and prints name, stars, city, and street.
        """
        hotel_name = input("Please enter the name of the hotel of which you would like to know the details: ")
        try:
            details = self.app.hotel_Manager.get_hotel_details(hotel_name)
        except ValueError as e:
            print(e)
            details = None
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
        try:
            rooms = self.app.room_Manager.get_rooms()
        except ValueError as e:
            print(e)
            rooms = []
        counter = 1
        for room in rooms:
            print(f"## {counter} ##")
            print(room.extendedStr())
            counter += 1
    
    def min_2_2(self, fromFunction:bool=False):
        name = ""
        while name == "":
            name = input("Please enter the hotel name in which you are looking for a room: ")
        hotels = [] 
        try:
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
            if check_in_date == "" :
                hotels = self.app.hotel_Manager.get_full_hotel(name)
            else:
                hotels = self.app.hotel_Manager.get_full_hotel(name, Format().parse(check_in_date), Format().parse(check_out_date))
        except ValueError as e:
            print(e)           
        
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
        try:
            status = self.app.hotel_Manager.add_hotel(name, stars, address_id)
        except ValueError as e:
            print(e)
            status = False
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
        
        try:
            hotel_id = int(input("Please name the Hotel ID of the hotel you would like to delete -> "))
            status = self.app.hotel_Manager.delete_hotel(hotel_id)
        except ValueError as e:
            print(e)
            status = False
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
        
        try:
            hotel_id = int(input("Please name the Hotel ID of the hotel, of which you\'d like to change the information to -> "))
            name = input("If you\'d like to change the name of the hotel please type it in, if you dont want to change the name, hit enter: ")
            stars = input("Please name the new amount of updated stars, if you dont want to change them, press enter: ")
            address_id = input("Please type the new Address ID, if you dont want to change the address, press enter: ")
            status = self.app.hotel_Manager.update_hotel(hotel_id, name, stars, address_id)
        except ValueError as e:
            print(e)
            status = False
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
            if user:
                try:
                    booking = self.app.booking_Manager.create_booking(user, rooms[int(inputnumber)-1], check_in, check_out)
                    if booking:
                        print(f"Success: Booking was created with id {booking.booking_id}")
                    else:
                        print("unfortunatelly, this did not work, please try again")
                except ValueError as e:
                    print(e)
                    print("Booking creation failed due to invalid input.")
            else:
                print("Login failed. Cannot create booking.")
        else:
            print("unfortunatelly, this did not work, please try again")    
        return self._prev_menu
    
    def min_5(self):
        """Creates and shows an invoice for a booking.

        Asks the user for a booking ID. If the booking is cancelled, no invoice is created.
        If successful, prints all invoice details. Otherwise, shows an error message.
        """
        try:
            booking_id = int(input("Please name the booking ID of which you\'d like to create an invoice"))
            e_mail = input("If you would like to receive an invoice by mail, you can enter the according e-mail here")
            result = self.app.invoice_Manager.create_invoice(booking_id, e_mail)
        except ValueError as e:
            print(e)
            result = None
        if result == "cancelled":
            print("This booking was cancelled, so there is not going to be an invoice")
        elif result == "no_booking":
            print("This booking does not exist")
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
    
    def min_6(self):
        user = self.login_user()
        if not user:
            ms = Mythic()
            ms.wtf()
            return UserStoryMenu(self.app, self)
        try:
            bookings = self.app.booking_Manager.get_bookings_from_user(user.guest_id) 
        except ValueError as e:
            print(e)
            bookings = []
        counter = 1
        for booking in bookings:
            print(f"{counter}. : {booking}")
            counter += 1
        try:
            choice = input("Which booking would you like to cancel? ")
            state = self.app.booking_Manager.update_booking(bookings[int(choice)-1], iscancelled=True)
            if state:
                print("Booking has been canceled")
                return UserStoryMenu(self.app, self)
            print("Something went wrong, please open support ticket on localhost:8080/support")
            UserStoryMenu(self.app, self)
        except ValueError as e: 
            print(f"Error processing cancellation: {e}")
        except IndexError:
            print("Invalid choice number.")
    
    def min_7(self):
        city = input("Please name the city in which you would like to stay")
        check_in_date = input("Please name you desired check-in date")
        check_out_date = input("Please name you desired check-out date")
        print("Thank you, we will now show you all avaiable rooms in this city with their price per night")
        time.sleep(3)
        try:
            rooms = self.app.room_Manager.get_available_rooms_city(city, check_in_date, check_out_date)
        except ValueError as e:
            print(e)
            rooms = []

        for room, price_per_night, name, room_type, nights_high_season, nights_off_season, total_price, average_price_per_night in rooms:
            print(f"{name} | Room ID: {room.room_id} | Type: {room_type}")
            print(f"Base price: {price_per_night:.2f} CHF | High season: {nights_high_season} nights | Off season: {nights_off_season} nights")
            print(f"Total: {total_price:.2f} CHF | Avg. price per night: {average_price_per_night:.2f} CHF")
            print("---------------------")

    
    def min_8(self, fromFunction:bool=False):
        if self._authenticate_admin():
            print("Shorty all bookings will be displayed")
            time.sleep(2)
            try:
                bookings = self.app.booking_Manager.get_all_bookings()
            except ValueError as e:
                print(e)
                bookings = []
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
            try:
                rooms = self.app.room_Manager.get_rooms()
            except ValueError as e:
                print(e)
                rooms = []
            print("---------------------")
            for room in rooms:
                print(room.extendedStr())
            print("---------------------")
    
    def min_10(self):
        if not self._authenticate_admin():
            ms = Mythic()
            ms.wtf()
            return UserStoryMenu(self.app,self._prev_menu)
        possibleValues = ["RoomType", "Facilities", "Rooms"]
        counter = 1
        for value in possibleValues:
            print(f"{counter}. {value}")
            counter += 1
        print(f"{counter}. back")
        choice = int(input("please enter your choice -> "))
        match choice:
            case 1:
                return Room_Type_Menu(self.app, self)
            case 2:
                return Facility_Menu(self.app, self)
            case 3:
                return Room_Menu(self.app, self)
            case 4:
                return UserStoryMenu(self.app, self._prev_menu)
            
    def db_1(self):
        bookings = self.min_8(fromFunction=True)
        counter = 1
        for hotel, booking in bookings:
            print(f"{counter}. {str(booking)}")
            counter += 1
        try:
            choice = input("Which booking would you like to alter? ")
            hotel,booking = bookings[int(choice)-1]
            phonenumber = int(input("Enter altered Phone number -> "))
            self.app.booking_Manager.update_booking(booking=booking,phonenumber=phonenumber)
        except ValueError as e:
            print(f"Error: {e}")
        except IndexError:
            print("Choice out of range.")
        return UserStoryMenu(self.app, self)
        
    def db_2(self):
        pass
    
    def db_2_1_1(self):
        def available_rooms(hotel_id):
            check_in_date = input("Please enter your check-in date: ")
            check_out_date = input("Please enter your check-out date: ")
            try:
                rooms_data = self.app.room_Manager.get_available_rooms_by_hotel_id(hotel_id, check_in_date, check_out_date)
            except ValueError as e:
                print(e)
                rooms_data = []

            if not rooms_data:
                print("Unfortunately there are no available rooms during your dates.")
                return UserStoryMenu(self.app)
            else:
                print("The following rooms are available:")
                room_selection = []
                room_ids = []
                for room, room_type, total_amount in rooms_data:
                    print(f"Room ID: {room.room_id}, Price per night: {room.price_per_night}, Type: {room_type.description}, Max guests: {room_type.maxGuests}, total amount: {total_amount}")
                    room_selection.append((room.room_id, float(total_amount)))
                    room_ids.append(room.room_id)
                    
                time.sleep(5)
                try:
                    room_id = int(input("Please enter the Room ID of the room you'd like to book: "))
                except ValueError as e:
                    print(f"Invalid input for Room ID: {e}")

                amount = next((amt for rid, amt in room_selection if rid == room_id), None)
                if amount is None:
                    print("Invalid Room ID.")
                    return UserStoryMenu(self.app)
                
            if room_id in room_ids:
                user_id = self._authentice_guest()
                if user_id:
                    guest_id = self.app.user_Manager.get_guest_id(user_id)
                    total_amount = amount
                    phone_number = input("If you would like to add a phone number, then plese enter this right here, else hit enter ")
                    try:
                        booking_id = self.app.booking_Manager.create_booking_new(guest_id, room_id, check_in_date, check_out_date, total_amount, phone_number)
                    except ValueError as e:
                        print(f"Error during booking creation: {e}")
                        return UserStoryMenu(self.app)
                    
                    if booking_id:
                        print(f"Your booking with the ID {booking_id.booking_id} is confirmed")
                    else:
                        print("Something went wrong, please try again")
                        return UserStoryMenu(self.app)
                else:
                    print("Your login credentials were wrong, please try again")
                    return UserStoryMenu(self.app)
            else:
                print("Sorry this room does not exist, please try again")
        def db_2_1_2(self):
            pass 


        hotel_name = input("Please enter the name of the hotel you'd like to book with:")
        hotels = self.app.hotel_Manager.get_hotel_details(hotel_name)
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
        uc = User_Manager()
        user_id = self._authentice_guest()
        if not user_id:
            print("Your login details were wrong, please try again")
            return UserStoryMenu(self.app)
        else:
            try:
                user_id = int(user_id)
                guest_id = self.app.user_Manager.get_guest_id(user_id)
            except ValueError as e:
                print(f"Invalid user ID: {e}")
            
            if not guest_id:
                print("Guest ID not found, please try again")
                return self
            try:
                all_bookings = self.app.booking_Manager.get_bookings_from_guest_id(guest_id)
            except ValueError as e:
                print(f"Error fetching bookings: {e}")
                return self

            if not all_bookings:
                print("No bookings found for your account.")
                return self
            else:
                print("Here are all your bookings:")
                for booking in all_bookings:
                    print(f"Booking ID: {booking.booking_id}")
                print("---------------------")
            booking_id = input("Please name your booking id, for which you'd like to leave a review: ")
            try:
                hotel_id = self.app.booking_Manager.check_user_id_matches_booking_id(booking_id, guest_id)
            except ValueError as e:
                print(f"Error checking booking ID: {e}")
                return self

            if not hotel_id:
                print("This is not your booking, please try again")
            else:
                score = input("Please leave your desired score, you can leave any number between 1 and 5: ")
                review = input("Please leave a comment reagarding your score: ")

                try:
                    status = self.app.rating_Manager.create_rating(booking_id, hotel_id, score, review)
                    if status:
                        print("Rating was created successfully")
                except ValueError as e:
                    print(f"Error: {e}")

    def db_4(self):
        print("\n--- Read Hotel Reviews ---")
        hotel_id_input = input("Enter the id of the hotel to see reviews (or leave blank to cancel): ")

        if not hotel_id_input.strip():
            print("Action canceled.")
            return self

        try:
            hotels_found = self.app.rating_Manager.get_ratings_for_hotel(hotel_id_input)
        except ValueError as e:
            print(f"Error fetching hotel ratings: {e}")
            return self

        if not hotels_found:
            print(f"No hotel found matching '{hotel_id_input}'.")
            input("\nPress Enter to return to the menu.")
            return self

        try:
            ratings = self.app.rating_Manager.get_ratings_for_hotel(str(hotel_id_input))
            if not ratings:
                print(f"\nNo reviews available for hotel '{hotel_id_input}'.")
            else:
                print(f"\n--- Reviews for {hotel_id_input} ---")
                for rating in ratings:
                    print(f"Date: {rating.get('created_at', 'N/A')}")
                    print(f"Score: {rating.get('score')}/5")
                    print(f"Comment: {rating.get('review', 'No Comment')}")
                    print("--------------------")
        except ValueError as e:
            print(f"Error fetching reviews: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        input("\nPress Enter to return to the menu.")
        return self

    def db_5(self):
        print("Why don't scientists trust atoms?")
        print("Because they make up everything!")
        self._not_implemented_yet()
        return self
    
    def db_6(self):
        print("Why did the scarecrow win an award?")
        print("Because he was outstanding in his field!")
        self._not_implemented_yet()
        return self
    
    def dv_1(self):
        if not self._authenticate_admin():
            return self

        print("Fetching room occupancy data...")
        occupancy_data = None
        try:
            occupancy_data = self.app.roomType_Manager.get_room_occupancy_data()
        except ValueError as e:
            print(f"Error fetching occupancy data: {e}")

        if occupancy_data and occupancy_data.get('room_type') and occupancy_data.get('count'):
            print("Displaying occupancy chart in a new window")
            main_tk_root = tk.Tk()
            main_tk_root.withdraw()
            chart = ChartView(self.app, occupancy_data, "occupancy")
            return chart.show_and_wait() 
        else:
            print("No occupancy data available to display.")
            if occupancy_data:
                print(f"Data received: {occupancy_data}")
            return self
    
    def dv_2(self):
        if not self._authenticate_admin():
            return self

        print("\nSelect demographic analysis to display:")
        print("1: Guest Age Distribution")
        print("2: Guest Country Distribution")
        print("3: Guest Booking Frequency (New vs. Returning)")
        choice = input("Enter your choice (1-3): ")

        data = None
        chart_type = None
        data_valid = False

        try:
            if choice == '1':
                print("Fetching guest age distribution data...")
                data = self.app.guest_Manager.get_guest_age_distribution_data()
                chart_type = "guest_age_histogram"
                if data and isinstance(data.get('ages'), list) and data['ages']:
                    data_valid = True
            elif choice == '2':
                print("Fetching guest country distribution data...")
                data = self.app.guest_Manager.get_guest_country_distribution_data()
                chart_type = "guest_country"
                if data and isinstance(data.get('countries'), list) and data['countries'] and isinstance(data.get('counts'), list) and len(data['countries']) == len(data['counts']):
                    data_valid = True
            elif choice == '3':
                print("Fetching guest booking frequency data...")
                data = self.app.guest_Manager.get_guest_booking_frequency_data()
                chart_type = "guest_booking_frequency"
                if data and isinstance(data.get('labels'), list) and data['labels'] and \
                   isinstance(data.get('sizes'), list) and sum(data['sizes']) > 0:
                    data_valid = True
            else:
                print("Invalid choice. Please select a number between 1 and 3.")
                return self
        except ValueError as e:
            print(f"Error fetching data for {chart_type if chart_type else 'selected analysis'}: {e}")
            data = None 
            data_valid = False

        if data_valid:
            print(f"Displaying {chart_type.replace('_', ' ')} chart in a new window.")
            main_tk_root = tk.Tk()
            main_tk_root.withdraw()
            chart_view = ChartView(self.app, data, chart_type) 
            return chart_view.show_and_wait()
        else:
            print(f"No valid data available to display for {chart_type.replace('_', ' ') if chart_type else 'the selected analysis'}.")
            if data is not None: 
                print(f"Data received but deemed invalid or empty: {data}")
            input("Press Enter to return to the menu.")
            return self
        
    def dv_3(self):
        if not self._authenticate_admin():
            input("Press Enter to return to the menu.")
            return self

        print("Fetching total revenue per hotel data...")
        data = None 
        try:
            data = self.app.hotel_Manager.get_amount_per_hotel()
        except ValueError as e:
            print(f"Error fetching total revenue data: {e}")
            
        chart_type = "total_revenue_per_hotel"
        data_valid = False

        if data and isinstance(data, list) and len(data) > 0:
            if all(isinstance(item, tuple) and len(item) == 2 and isinstance(item[0], str) and isinstance(item[1], (int, float)) for item in data):
                data_valid = True
        
        if data_valid:
            print(f"Displaying {chart_type.replace('_', ' ')} chart in a new window.")
            main_tk_root = tk.Tk()
            main_tk_root.withdraw()
            chart_view = ChartView(self.app, data, chart_type) 
            return chart_view.show_and_wait()
        else:
            print(f"No valid data available to display for {chart_type.replace('_', ' ')}.")
            if data is not None: 
                print(f"Data received but deemed invalid or empty: {data}")
            input("Press Enter to return to the menu.")
            return self

    def opt_1(self):
        self.dv_3()
    
    def opt_2(self):
        print("What do you call fake spaghetti?")
        print("An impasta!")
        self._not_implemented_yet()
        return self
    
    def opt_3(self):
        print("Why did the bicycle fall over?")
        print("Because it was two tired!")
        self._not_implemented_yet()
        return self
    
    def opt_4(self):
        self.min_5()

    def back(self):
        return self._prev_menu

    def login_user(self) -> User:
        id = int(input("Please provide user id: "))
        password = input("Please provide password: ")
        return self.app.user_Manager.login_user(id, password)