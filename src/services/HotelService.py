import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from controller.Validator import Validator
from models.Hotels import Hotel
from controller.DataBaseController import DataBaseController
from datetime import date
from handlers.UserHandler import Userhandler

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
            print(f"{hotel.name} has {hotel.stars} stars and is located in {city}")

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
            print(f"{hotel.name} has {hotel.stars} stars and is located in {city}")
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
            print(f"{hotel.name} has {hotel.stars} stars and is located in {city}")


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
        for row in result: 
            data = dict(row)
            hotel = Hotel(
            hotel_id = data["hotel_id"],
            name = data["name"],
            stars = data["stars"]    
            )
            hotels.append(hotel)
        for hotel in hotels: 
            print(f"{hotel.name} has {hotel.stars} stars and is located in {city}")

    def get_selected_filters(self, city="all", min_stars="all", guests="all", check_in_date="all", check_out_date="all"): #All als Default Wert, damit nachher einfach die nicht gewünschten Werte weggelassen werden können bzw. nichts eingegeben werden muss
        query = """
        SELECT DISTINCT hotel_id, name, stars, city, street
        FROM extended_hotel_room_booking
        WHERE 1=1
        """ #1=1 ist dafür, dass später alle modularen Abfragen mit AND geschrieben werden können, 1=1 ist immer true, also wenn nichts gefiltert werden einfach alle Hotels angezeigt
        parameters = []
        if city != "all":
            query += " AND city = ?"
            parameters.append(city)
        if min_stars != "all":
            query += " AND stars >= ? "
            parameters.append(min_stars)
        if guests != "all":
            query += " AND max_guests >= ?"
            parameters.append(guests)
        if (check_in_date != "all" and check_out_date == "all") or (check_in_date == "all" and check_out_date != "all"):
            raise ValueError("If you provide a check-in-date, you must provide a check-out-date and the other way around")  
        elif check_in_date != "all" and check_out_date != "all":
            query += """
                    AND room_id NOT IN (SELECT room_id
                    FROM extended_hotel_room_booking
                    WHERE (check_in_date BETWEEN ? AND ?)
                    OR (check_out_date BETWEEN ? AND ?)
                    OR (check_in_date <= ? AND check_out_date >= ?))
                    """
            parameters.append(check_in_date)
            parameters.append(check_out_date)
            parameters.append(check_in_date)
            parameters.append(check_out_date)
            parameters.append(check_in_date)
            parameters.append(check_out_date)
        result = self.db.fetchall(query,parameters)
        hotels = []
        for row in result:
            data = dict(row)
            hotel = Hotel(
            hotel_id = data["hotel_id"],
            name = data["name"],
            stars = data["stars"]    
            )
            hotels.append((hotel, data["city"], data["street"]))

        for hotel, city, street in hotels:
            print(f"{hotel.name} has {hotel.stars} stars, is located in {city} at: {street}")
    def get_hotel_details(self, hotel_name):
        query = """
        SELECT DISTINCT hotel_id, name, stars, street, city 
        FROM extended_hotel_room
        WHERE name = ?       
        """
        result = self.db.fetchall(query, (hotel_name,))
        hotels = []
        for row in result: 
            data = dict(row)
            hotel = Hotel(hotel_id = data["hotel_id"], name = data["name"], stars = data["stars"])
            street = data["street"]
            city = data["city"]
            hotels.append((hotel, data["street"], data["city"]))
        for hotel, street, city in hotels: 
            print(f"The hotel {hotel.name} you mentioned has {hotel.stars} stars and is located in {city} at {street}")
    
    def add_hotel(self, user_id, password, name, stars, address_id):
        uh = Userhandler()
        if uh.check_admin(user_id, password) != True:
            raise ValueError("You need admin rights to perform this action")
        else:
            query_max_id = """
            SELECT MAX(hotel_id) FROM Hotel
            """
            result_max = self.db.fetchone(query_max_id)[0]
            if result_max is None:
                result_max = 0
            query_add_hotel = """
            INSERT INTO Hotel
            VALUES (?, ?, ?, ?)
            """
            self.db.execute(query_add_hotel,(result_max + 1, name, stars, address_id))
            print("Hotel was added successfuly")

    def delete_hotel(self, user_id, password, hotel_id):
        uh = Userhandler()
        if uh.check_admin(user_id, password) != True:
            raise ValueError("You need admin rights to perform this action")
        else:
            query = """
            DELETE
            FROM Hotel 
            WHERE hotel_id = ?
            """
            rows_deleted = self.db.execute(query, (hotel_id,)).rowcount
            if rows_deleted <1:
                print("There is no hotel with this hotel ID")
            else:
                print("The hotel was deleted successfuly")


# Nutzung User Story 1.1
hotels = Hotelservice()
hotels.get_hotel_in_city("Zürich")
# Nutzung User Story 1.2
story2 = Hotelservice()
story2.get_hotel_in_city_stars("Zürich", 3)
# Nutzung User Story 1.3
story3 = Hotelservice()
story3.get_hotel_in_city_stars_guests("Zürich", 4, 1)
# Nutzung User Story 1.4
story4 = Hotelservice()
story4.get_hotel_in_city_booking("Zürich", 3, 1, "2026-05-05", "2026-06-06")
#Nutzung User Story 1.5
story5 = Hotelservice()
story5.get_selected_filters("all",3,"all", "all", "all")

#Nutzung User Story 1.6
story6 = Hotelservice()
story6.get_hotel_details("Hotel Baur au Lac")

#Nutzung User Story 3.1
story31 = Hotelservice()
story31.add_hotel(6, "admin", "Hotel Yves", 5, 2)
#Nutzung User Story 3.2
story32 = Hotelservice()
story32.delete_hotel(6, "admin", 7)