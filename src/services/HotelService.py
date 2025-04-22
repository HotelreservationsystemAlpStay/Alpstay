import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from controller.Validator import Validator
from models.Hotels import Hotel
from controller.DataBaseController import DataBaseController

class Hotelservice:
    def __init__(self): 
        self.db = DataBaseController()

    def get_hotel_in_city(self, city):
        query = """
        SELECT h.hotel_id, h.name, h.stars
        FROM Hotel h 
        JOIN Address a ON h.address_id = a.address_id 
        WHERE a.city = ?
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
        Validator.checkInteger(min_stars, "Sterne")
        Validator.checkStars(min_stars)
        query = """
        SELECT h.hotel_id, h.name, h.stars
        FROM Hotel h 
        JOIN Address a ON h.address_id = a.address_id 
        WHERE a.city = ?
        AND h.stars >= ?
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

# Nutzung User Story 1
hotels = Hotelservice()
hotels.get_hotel_in_city("Bern")
# Nutzung User Story 2 
story2 = Hotelservice()
story2.get_hotel_in_city_stars("Zürich", 4)

