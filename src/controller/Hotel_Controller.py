from utils.Validator import Validator
from data_Access.Hotel_Access import Hotel_Access
from data_Access.Address_Access import Address_access
from models.Hotels import Hotel
from controller.User_Controller import User_Controller
from controller.Room_Controller import RoomController
from utils.Formatting import Format
from datetime import date, datetime

class Hotel_Controller:
    def __init__(self):
        self.hotel_access = Hotel_Access()
    
    @staticmethod
    def _sqlite3row_to_hotel(row, address):
        return Hotel(
            hotel_id=row["hotel_id"],
            name=row["name"],
            stars=row["stars"],
            address=address
        )

    def get_hotel_in_city(self, city):
        """Returns all hotels in a given city

        Args:
            city (str): Name of the city

        Returns:
            list[Hotel]: List of Hotel objects in the specified city
        """
        Validator.checkStr(city, "city")
        result = self.hotel_access.access_hotel_in_city(city)
        return result
    
    def get_hotel_in_city_stars(self, city, min_stars):
        """Returns all hotels in a city with at least the given number of stars

        Args:
            city (str): Name of the city
            min_stars (int): Minimum number of stars the hotel must have

        Returns:
            list[Hotel]: List of Hotel objects matching the criteria
        """
        Validator.checkStr(city, "city")
        Validator.checkStars(min_stars)
        return self.hotel_access.access_hotel_in_city_stars(city, min_stars)
    
    def get_hotel_in_city_stars_guests(self, city, min_stars, guests):
        """Returns all hotels in a city with at least the given number of stars and enough capacity for the specified number of guests

        Args:
            city (str): Name of the city
            min_stars (int): Minimum number of stars the hotel must have
            guests (int): Minimum number of guests the hotel must accommodate

        Returns:
            list[Hotel]: List of Hotel objects matching the criteria
        """
        Validator.checkStr(city, "city")
        Validator.checkStars(min_stars)
        Validator.checkPositiveInteger(guests, "Guests")
        return self.hotel_access.access_hotel_in_city_stars_guests(city, min_stars, guests)

    
    def get_hotel_in_city_booking(self, city, min_stars, guests, check_in_date, check_out_date):
        """Returns all hotels in a city that match minimum stars and guest requirements, and have available rooms in the given date range

        Args:
            city (str): Name of the city
            min_stars (int): Minimum number of stars the hotel must have
            guests (int): Minimum number of guests the hotel must accommodate
            check_in_date (str): Check-in date in string format
            check_out_date (str): Check-out date in string format

        Returns:
            list[Hotel]: List of Hotel objects available in the given date range and matching the criteria
        """
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
        return result
    
    def get_selected_filters(self, city, min_stars, guests, check_in_date, check_out_date):
        """Returns all hotels that match the given optional filters: city, minimum stars, guests, and date range

        All filters are optional, but check-in and check-out dates must be provided together.

        However at least one filter needs to be provided. 

        Args:
            city (str or None): Name of the city (optional)
            min_stars (int or None): Minimum number of stars (optional)
            guests (int or None): Minimum number of guests (optional)
            check_in_date (str or None): Check-in date (optional, must be used with check_out_date)
            check_out_date (str or None): Check-out date (optional, must be used with check_in_date)

        Returns:
            list[Hotel]: List of Hotel objects matching the given filters
        """
        if city:
            Validator.checkStr(city, "city")
        if min_stars:
            min_stars = int(min_stars)
            Validator.checkStars(min_stars)
        if guests:
            guests = int(guests)
            Validator.checkPositiveInteger(guests, "Guests")
        if (not check_in_date and check_out_date) or (check_in_date and not check_out_date):
            raise ValueError("If you provide a check-in-date, you must provide a check-out-date and the other way around, please try again")  
        elif check_in_date and check_out_date:
            check_in_date = Format().parse(check_in_date)
            check_out_date = Format().parse(check_out_date)
            Validator.checkDate(check_in_date, "Check-in date")
            Validator.checkDate(check_out_date, "Check-out date")
            Validator.checkDateDifference(check_in_date, check_out_date)
        elif not city and not min_stars and not guests and not check_in_date and not check_out_date:
            raise ValueError("You must provide at least one filter, please try again")
        result = self.hotel_access.access_selected_filters(city, min_stars, guests, check_in_date, check_out_date)
        return result
    
    def get_hotel_details(self, hotel_name):
        """Returns detailed hotel information including address data for a given hotel name

        Args:
            hotel_name (str): Name of the hotel

        Returns:
            list[tuple[Hotel, str, str]]: List of tuples containing Hotel object, street, and city
        """
        result = self.hotel_access.access_hotel_details(hotel_name)
        if not result:
            return False
        else:
            return result
    
    def get_full_hotel(self, hotel_name:str, start_date:date = None, end_date:date = None):
        """Returns full hotel with address and rooms, for the moment only 1 Hotel but able to expand

        Args:
            hotel_name (str): 
            start_date (date, optional): Defaults to None.
            end_date (date, optional): Defaults to None.

        Returns:
            list[Hotels]: List of hotels
        """
        result = self.hotel_access.access_hotel_details(hotel_name)
        hotels = []
        for res in result:
            hotels.append(self._sqlite3row_to_hotel(row=res,address=Address_access().sqlite3row_to_address(res)))
        print(len(hotels))
        for hotel in hotels:
            hotel.rooms = RoomController().get_rooms(dateStart=start_date, dateEnd=end_date, hotel_ids=[hotel.hotel_id])
        return hotels

    def add_hotel(self, name, stars, address_id):
        """Adds a new hotel to the database

        Args:
            name (str): Name of the hotel
            stars (int): Star rating of the hotel
            address_id (int): ID of the associated address

        Returns:
            bool: True if the hotel was added successfully, False otherwise
        """
        status = self.hotel_access.access_add_hotel(name, stars, address_id)
        return status

    def delete_hotel(self, hotel_id):
        """Deletes a hotel from the database by its ID

        Args:
            hotel_id (int): ID of the hotel to delete

        Returns:
            bool: True if the hotel was deleted successfully, False otherwise
        """
        status = self.hotel_access.access_delete_hotel(hotel_id)
        return status
    
    def update_hotel(self, hotel_id, name, stars, address_id):
        """Updates hotel information, at least one field must be changed

        Args:
            hotel_id (int): ID of the hotel to update
            name (str or None): New name of the hotel (optional)
            stars (int or None): New star rating (optional)
            address_id (int or None): New address ID (optional)

        Raises:
            ValueError: If no fields are provided for update

        Returns:
            bool: True if the hotel was updated successfully, False otherwise
        """
        if not name and not stars and not address_id:
            raise ValueError("You must change at least one information")
        if stars:
            stars = int(stars)
        if address_id:
            address_id = int(address_id)
        return self.hotel_access.access_update_hotel(hotel_id, name, stars, address_id)
    


