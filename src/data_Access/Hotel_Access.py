from data_Access.Base_Access_Controller import Base_Access_Controller
from data_Access.Address_Access import Address_Access
from datetime import date
from models.Hotels import Hotel
import sqlite3

class Hotel_Access:
    def __init__(self): 
        """Initialize Hotel Access with database controller."""
        self.db = Base_Access_Controller()

    def _sqlite3row_to_hotel(self, row:sqlite3.Row):
        """Convert SQLite row to Hotel object."""
        return Hotel(
            hotel_id=int(row['hotel_id']),
            name=row['name'],
            stars=row['stars']
        )

    def access_hotel_in_city(self, city):
        """Get all hotels in a specific city.
        
        Args:
            city (str): Name of the city
            
        Returns:
            list[Hotel]: List of hotels in the city
        """
        query = """
        SELECT hotel_id, name, stars
        FROM extended_hotel
        WHERE city = ?
        """
        result = self.db.fetchall(query, (city,))
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
    
    def access_hotel_in_city_stars(self, city, min_stars):
        """Get hotels in a city with minimum star rating.
        
        Args:
            city (str): Name of the city
            min_stars (int): Minimum star rating
            
        Returns:
            list[Hotel]: List of hotels meeting the criteria
        """
        query = """
        SELECT hotel_id, name, stars
        FROM extended_hotel
        WHERE city = ? 
        AND stars >= ?
        """
        result =  self.db.fetchall(query, (city, min_stars))
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

    def access_hotel_in_city_stars_guests(self, city, min_stars, guests):
        """Get hotels in a city with minimum star rating and guest capacity.
        
        Args:
            city (str): Name of the city
            min_stars (int): Minimum star rating
            guests (int): Minimum number of guests
            
        Returns:
            list[Hotel]: List of hotels meeting the criteria
        """
        query = """
        SELECT hotel_id, name, stars
        FROM extended_hotel_room
        WHERE city = ? 
        AND stars >= ?
        AND max_guests >= ? 
        """
        result =  self.db.fetchall(query, (city, min_stars, guests))
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

    def access_hotel_in_city_booking(self, city, min_stars, guests, check_in_date, check_out_date):
        """Get available hotels in a city for booking based on criteria.
        
        Args:
            city (str): Name of the city
            min_stars (int): Minimum star rating
            guests (int): Number of guests
            check_in_date (date): Check-in date
            check_out_date (date): Check-out date
            
        Returns:
            list[Hotel]: List of available hotels for the given dates
        """
        query = """
        SELECT DISTINCT hotel_id, name, stars
        FROM extended_hotel_room_booking
        WHERE room_id IS NOT NULL
        AND city = ? 
        AND stars >= ?
        AND max_guests >= ?
        AND room_id NOT IN (
        SELECT room_id
        FROM extended_hotel_room_booking
        WHERE is_cancelled = 0
        AND(
        (check_in_date BETWEEN ? AND ?)
        OR (check_out_date BETWEEN ? AND ?)
        OR (check_in_date <= ? AND check_out_date >= ?)
        ))
        """
        params = (
            city, min_stars, guests,
            check_in_date, check_out_date,
            check_in_date, check_out_date,
            check_in_date, check_out_date
        )
        result = self.db.fetchall(query, params)
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

    def access_selected_filters(self, city, min_stars, guests, check_in_date, check_out_date):
        """Get hotels based on selected filters.
        
        Args:
            city (str): Name of the city
            min_stars (int): Minimum star rating
            guests (int): Number of guests
            check_in_date (date): Check-in date
            check_out_date (date): Check-out date
            
        Returns:
            list[Hotel]: List of hotels meeting the filter criteria
        """
        query = """
        SELECT DISTINCT hotel_id, name, stars, city, street, address_id, zip_code
        FROM extended_hotel_room_booking
        WHERE room_id IS NOT NULL
        """
        parameters = []

        if city:
            query += " AND city = ?"
            parameters.append(city)
        if min_stars:
            query += " AND stars >= ? "
            parameters.append(min_stars)
        if guests:
            query += " AND max_guests >= ?"
            parameters.append(guests)
        if check_in_date and check_out_date:
            query += """
                    AND room_id NOT IN (SELECT room_id
                    FROM extended_hotel_room_booking
                    WHERE is_cancelled = 0
                    AND (
                    (check_in_date BETWEEN ? AND ?)
                    OR (check_out_date BETWEEN ? AND ?)
                    OR (check_in_date <= ? AND check_out_date >= ?))
                    )
                    """
            parameters.append(check_in_date)
            parameters.append(check_out_date)
            parameters.append(check_in_date)
            parameters.append(check_out_date)
            parameters.append(check_in_date)
            parameters.append(check_out_date)
        result = self.db.fetchall(query, parameters)
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


    def access_hotel_details(self, hotel_name):
        """Get detailed information about a specific hotel.
        
        Args:
            hotel_name (str): Name of the hotel
            
        Returns:
            list[tuple]: List of tuples containing hotel and address details
        """
        query = """
        SELECT DISTINCT hotel_id, name, stars, address_id, street, city, zip_code
        FROM extended_hotel_room
        WHERE (name) = (?)       
        """
        result = self.db.fetchall(query, (hotel_name,))
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
    
    def access_hotel_detailed_address(self, hotel_name):
        """Get hotel details along with the full address.
        
        Args:
            hotel_name (str): Name of the hotel
            
        Returns:
            list[Hotel]: List of hotel objects with detailed address
        """
        query = """
        SELECT DISTINCT hotel_id, name, stars, address_id, street, city, zip_code
        FROM extended_hotel_room
        WHERE name = ?
        """
        result = self.db.fetchall(query, (hotel_name,))
        hotels = []
        for row in result: 
            hotel = self._sqlite3row_to_hotel(row)
            hotel.address = Address_Access().sqlite3row_to_address(row)
            hotels.append(hotel)
        return hotels
    
    def access_add_hotel(self, name, stars, address_id):
        """Add a new hotel to the database.
        
        Args:
            name (str): Name of the hotel
            stars (int): Star rating of the hotel
            address_id (int): Address ID for the hotel
            
        Returns:
            bool: True if hotel was added, False otherwise
        """

        query_add_hotel = """
        INSERT INTO Hotel (name, stars, address_id)
        VALUES (?, ?, ?)
        """
        self.db.execute(query_add_hotel, (name, stars, address_id))
        return True


    def access_delete_hotel(self, hotel_id):
        """Delete a hotel from the database.
        
        Args:
            hotel_id (int): ID of the hotel to be deleted
            
        Returns:
            bool: True if hotel was deleted, False otherwise
        """
        query = """
        DELETE
        FROM Hotel 
        WHERE hotel_id = ?
        """
        rows_deleted = self.db.execute(query, (hotel_id,)).rowcount
        if rows_deleted < 1:
            return False
        else:
            return True

    def access_update_hotel(self, hotel_id, name, stars, address_id):
        """Update hotel information in the database.
        
        Args:
            hotel_id (int): ID of the hotel to be updated
            name (str): New name for the hotel
            stars (int): New star rating for the hotel
            address_id (int): New address ID for the hotel
            
        Returns:
            bool: True if hotel was updated, False otherwise
        """
        query = "UPDATE Hotel SET "
        fields = []
        parameters = []

        if name:
            fields.append("name = ?")
            parameters.append(name)
        if stars:
            fields.append("stars = ?")
            parameters.append(stars)
        if address_id:
            fields.append("address_id = ?")
            parameters.append(address_id)

        query += ", ".join(fields)
        query += " WHERE hotel_id = ?"
        parameters.append(hotel_id)

        result = self.db.execute(query, tuple(parameters))
        if result.rowcount == 0:
            return False
        else:
            return True

    def amount_per_hotel(self):
        """Get the total amount per hotel from bookings.
        
        Returns:
            list: List of hotels with the total amount from bookings
        """
        query = """
        SELECT name, SUM(total_amount) 
        FROM booking_view 
        GROUP BY name
        HAVING SUM(total_amount) > 0
        """
        return self.db.fetchall(query)
    


    
    #????  - Wer macht das und wo wird es gebraucht und wieso ist das in Hotel_access
    #def get_available_rooms(self, dateStart:date=None, dateEnd:date=None, hotel:Hotel=None, roomType:RoomType=None) -> list | list[Room]:
    #roomAccess = Room_Access()
    #if not hotel: return []
    #return roomAccess.get_rooms(dateStart, dateEnd, [hotel.hotel_id], roomType)
"""
# Nutzung User Story 1.1
hotels = Hotel_Access()
hotels.get_hotel_in_city("Zürich")
# Nutzung User Story 1.2
story2 = Hotel_Access()
story2.get_hotel_in_city_stars("Zürich", 3)
# Nutzung User Story 1.3
story3 = Hotel_Access()
story3.get_hotel_in_city_stars_guests("Zürich", 4, 1)
# Nutzung User Story 1.4
story4 = Hotel_Access()
story4.get_hotel_in_city_booking("Bern", 3, 1, date(2022,5,5), date(2026,6,6))
#Nutzung User Story 1.5
story5 = Hotel_Access()
story5.get_selected_filters("all",3,"all", "all", "all")

#Nutzung User Story 1.6
story6 = Hotel_Access()
story6.get_hotel_details("Hotel Baur au Lac")
"""



"""
#Nutzung User Story 3.1
story31 = Hotel_Access()
story31.add_hotel(6, "admin", "Hotel Yves", 5, 2)
#Nutzung User Story 3.2
story32 = Hotel_Access()
story32.delete_hotel(6, "admin", 7)
#Nutzung User Story 3.3
story33 = Hotel_Access()
story33.update_hotel(6, "admin", 7, "Hotel Lustighof")
"""