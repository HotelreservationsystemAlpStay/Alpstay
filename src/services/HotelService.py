import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from controller.Validator import Validator
from models.Hotels import Hotel
from controller.DataBaseController import DataBaseController
from datetime import date

class Hotelservice:
    def __init__(self): 
        self.db = DataBaseController()

    def get_hotel_in_city(self, city):
        query = """
        SELECT hotel_id, name, stars
        FROM extended_hotel
        WHERE city = ?
        """
        result = self.db.fetchall(query, (city,)) #bei fetchall ist definiert, dass alle ? mit den Parametern in der Tupel ersetzt werden, hier also city, aber achtung Reihenfolge muss stimmen
        hotels = [] #leere Liste wird erstellt, die dann mit dem for loop gefüllt wird
        for row in result:
            data = dict(row) #dict macht den Output von SQLite lesbar, Daten von Hotel werden in data gespeichert
            hotel = Hotel( 
                hotel_id=data["hotel_id"], 
                name=data["name"],
                stars=data["stars"]
            )     #In diesem Block wird die Klasse Hotel aufgerufen, deshalb muss man hotel_id definieren, muss aber nicht verwendet werden
            hotels.append(hotel) #Liste wird ergänzt um Hotel
        for hotel in hotels:
            print(f"{hotel.name} hat {hotel.stars} Sterne und liegt in {city}")

    def get_hotel_in_city_stars(self, city, min_stars):
        Validator.checkStars(min_stars)
        query = """
        SELECT hotel_id, name, stars
        FROM extended_hotel
        WHERE city = ? 
        AND stars >= ?
        """
        result = self.db.fetchall(query, (city, min_stars))
        hotels = []
        for row in result: 
            data = dict(row)
            hotel = Hotel(
            hotel_id = data["hotel_id"],
            name = data["name"],
            stars = data["stars"]
            )
            hotels.append(hotel)
        for hotel in hotels:
            print(f"{hotel.name} hat {hotel.stars} Sterne und liegt in {city}")
    def get_hotel_in_city_stars_guests(self, city, min_stars, guests):
        Validator.checkStars(min_stars)
        query = """
        SELECT hotel_id, name, stars
        FROM extended_hotel_room
        WHERE city = ? 
        AND stars >= ?
        AND max_guests >= ? 
        """
        result = self.db.fetchall(query, (city, min_stars, guests))
        hotels = []
        for row in result:
            data = dict(row)
            hotel = Hotel(
            hotel_id = data["hotel_id"],
            name = data["name"],
            stars = data["stars"]
            )
            hotels.append(hotel)
        for hotel in hotels:
            print(f"{hotel.name} hat {hotel.stars} Sterne und liegt in {city}")


#User Story 4 müsste eigentlich stars und guests nicht enthalten, habe es trotzdem mal drin gelassen 
    def get_hotel_in_city_booking(self, city, min_stars, guests, check_in_date, check_out_date):
        Validator.checkStars(min_stars)
        query = """
        SELECT DISTINCT hotel_id, name, stars
        FROM extended_hotel_room_booking
        WHERE city = ? 
        AND stars >= ?
        AND max_guests >= ?
        AND room_id NOT IN (SELECT room_id
        FROM extended_hotel_room_booking
        WHERE (check_in_date BETWEEN ? AND ?)
        OR (check_out_date BETWEEN ? AND ?)
        OR (check_in_date <= ? AND check_out_date >= ?))
        """
        result = self.db.fetchall(query, (city, min_stars, guests, check_in_date, check_out_date, check_in_date, check_out_date, check_in_date, check_out_date))
        hotels = []
        for hotel in result: 
            data = dict(hotel)
            hotel = Hotel(
            hotel_id = data["hotel_id"],
            name = data["name"],
            stars = data["stars"]    
            )
            hotels.append(hotel)
        for hotel in hotels: 
            print(f"{hotel.name} hat {hotel.stars} Sterne und liegt in {city}")



# Nutzung User Story 1
hotels = Hotelservice()
hotels.get_hotel_in_city("Zürich")
# Nutzung User Story 2 
story2 = Hotelservice()
story2.get_hotel_in_city_stars("Zürich", 3)
# Nutzung User Story 3 
story3 = Hotelservice()
story3.get_hotel_in_city_stars_guests("Zürich", 4, 1)
# Nutzung User Story 4
story4 = Hotelservice()
story4.get_hotel_in_city_booking("Bern", 2, 2, "2024-05-05", "2026-06-06")

