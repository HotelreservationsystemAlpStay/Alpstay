from data_Access.Room_Access import Room_Access
from models.Room import Room
from models.Room_Type import Room_Type
from datetime import date
from datetime import timedelta
from utils.Formatting import Format
from utils.Validator import Validator

class Room_Manager():
    def __init__(self):
        """Initialize Room Manager with Room Access layer."""
        self.room_Access = Room_Access()
    
    def get_rooms(self, dateStart: date = None, dateEnd: date = None, hotel_ids: list[int] = None, Room_Type:Room_Type = None)->list[Room]:
        """Get rooms with optional filters.

        Args:
            dateStart (date, optional): Start date filter
            dateEnd (date, optional): End date filter
            hotel_ids (list[int], optional): List of hotel IDs to filter by
            Room_Type (Room_Type, optional): Room type filter

        Returns:
            list[Room]: List of rooms matching the criteria
        """
        return self.room_Access.get_rooms(dateStart=dateStart, dateEnd=dateEnd, hotel_ids=hotel_ids, room_Type=Room_Type)
    
    def update_room(self, room:Room):
        """Update room information in the database.

        Args:
            room (Room): Room object with updated information

        Returns:
            Updated room object
        """
        return self.room_Access.updateRoom(room)
    
    def get_available_rooms_city(self, city:str, check_in_date:str, check_out_date:str):
        """Get available rooms in a city with dynamic pricing.

        Args:
            city (str): Name of the city
            check_in_date (str): Check-in date as string
            check_out_date (str): Check-out date as string

        Returns:
            list: List of tuples containing room and pricing information
        """
        check_in_date = Format.parse(check_in_date)
        check_out_date = Format.parse(check_out_date)
        list = self.room_Access.get_available_rooms_city(city, check_in_date, check_out_date)
        hotels = []
        for result in list:
            data = dict(result)
            room_id = data["room_id"]
            room_no = data["room_number"]
            price_per_night = data["price_per_night"]
            room = Room(room_id, room_no, price_per_night)
            name = data["name"]
            room_type = data["room_type"]

            nights_high_season = 0
            current = check_in_date
            while current < check_out_date:
                if 5 <= current.month <= 9:
                    nights_high_season += 1
                current += timedelta(days=1)
            nights_offseason = (check_out_date - check_in_date).days - nights_high_season
            total_price = nights_high_season * price_per_night * 1.2 + nights_offseason * price_per_night * 0.8
            average_price_per_night = total_price/(nights_high_season+nights_offseason)
            hotels.append((room, price_per_night, name, room_type, nights_high_season, nights_offseason, total_price, average_price_per_night))
        return hotels
    
    def get_available_rooms_by_hotel_id(self, hotel_id, check_in_date, check_out_date):
        """Get available rooms for a specific hotel in a date range.

        Args:
            hotel_id: ID of the hotel
            check_in_date: Check-in date as string
            check_out_date: Check-out date as string

        Returns:
            list: List of tuples containing (room, room_type, total_amount)
        """
        check_in_date = Format.parse(check_in_date)
        check_out_date = Format.parse(check_out_date)
        Validator.checkDateDifference(check_in_date, check_out_date)
        rooms = self.room_Access.access_available_rooms_hotel_id(hotel_id, check_in_date, check_out_date)
        nights = (check_out_date - check_in_date).days
        results = []
        for room, room_type in rooms:
            total_amount = room.price_per_night * nights
            results.append((room, room_type, total_amount))
        return results