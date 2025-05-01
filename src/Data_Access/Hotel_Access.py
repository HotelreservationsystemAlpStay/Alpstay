import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.Validator import Validator
from models.Hotels import Hotel
from Base_Access_Controller import Base_Access_Controller
from datetime import date
from controller.User_Controller import User_Controller

class Hotel_Access:
    def __init__(self): 
        self.db = Base_Access_Controller()

    def get_hotel_in_city(self, city):
        Validator.checkStr(city, "city")
        query = """
        SELECT hotel_id, name, stars
        FROM extended_hotel
        WHERE city = ?
        """
        result = self.db.fetchall(query, (city,)) #bei fetchall ist definiert, dass alle ? mit den Parametern in der Tupel ersetzt werden, hier also city, aber achtung Reihenfolge muss stimmen
        if not result:
            print("Unfortunately there are no hotels in the city you mentioned")
        else:
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
        Validator.checkStr(city, "city")
        Validator.checkStars(min_stars)
        query = """
        SELECT hotel_id, name, stars
        FROM extended_hotel
        WHERE city = ? 
        AND stars >= ?
        """
        result = self.db.fetchall(query, (city, min_stars))
        if not result:
            print("Unfortunately there are no hotels which match your filters")
        else:
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
        Validator.checkStr(city, "city")
        Validator.checkStars(min_stars)
        Validator.checkPositiveInteger(guests, "Guests")
        query = """
        SELECT hotel_id, name, stars
        FROM extended_hotel_room
        WHERE city = ? 
        AND stars >= ?
        AND max_guests >= ? 
        """
        result = self.db.fetchall(query, (city, min_stars, guests))
        if not result:
            print("Unfortunately there are no hotels which match your filters")
        else:
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
        Validator.checkStr(city, "city")
        Validator.checkStars(min_stars)
        Validator.checkPositiveInteger(guests, "Guests")
        Validator.checkDate(check_in_date, "Check-in date")
        Validator.checkDate(check_out_date, "Check-out date")
        Validator.checkDateDifference(check_in_date, check_out_date)
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
        if not result:
            print("Unfortunately there are no hotels which match your filters")
        else:
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
            Validator.checkStr(city, "city")
        if min_stars != "all":
            query += " AND stars >= ? "
            parameters.append(min_stars)
            Validator.checkStars(min_stars)
        if guests != "all":
            query += " AND max_guests >= ?"
            parameters.append(guests)
            Validator.checkPositiveInteger(guests, "Guests")
        if (check_in_date != "all" and check_out_date == "all") or (check_in_date == "all" and check_out_date != "all"):
            raise ValueError("If you provide a check-in-date, you must provide a check-out-date and the other way around")  
        elif check_in_date != "all" and check_out_date != "all":
            Validator.checkDate(check_in_date, "Check-in date")
            Validator.checkDate(check_out_date, "Check-out date")
            Validator.checkDateDifference(check_in_date, check_out_date)
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
        if not result:
            print("Unfortunately there are no hotels which match your filters")
        else:
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
        if not result:
            print("Unfortunately there are no hotels which match your filters")
        else:
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
        uh = User_Controller()
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
        uh = User_Controller()
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
    def update_hotel(self, user_id, password, hotel_id, name=None, stars=None, address_id=None):
        uh = User_Controller
        if uh.check_admin(user_id, password) != True:
            raise ValueError("You need admin rights to perform this action")
        if not hotel_id:
            raise ValueError("You must provide the hotel ID of the hotel you would like to change")
        if name is None and stars is None and address_id is None:
            raise ValueError("You must change at least one information of the hotel")

        query = "UPDATE Hotel SET "
        fields = []
        parameters = []

        if name is not None:
            fields.append("name = ?")
            parameters.append(name)
        if stars is not None:
            fields.append("stars = ?")
            parameters.append(stars)
        if address_id is not None:
            fields.append("address_id = ?")
            parameters.append(address_id)

        query += ", ".join(fields)
        query += " WHERE hotel_id = ?"
        parameters.append(hotel_id)

        result = self.db.execute(query, tuple(parameters))
        if result.rowcount == 0:
            print("No hotel matches your hotel ID")
        else:
            print("Changed Hotel Information successfully")





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
story4.get_hotel_in_city_booking("Bern", 3, 1, date(2022,5,5), date(2026,6,6))
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
#Nutzung User Story 3.3
story33 = Hotelservice()
story33.update_hotel(6, "admin", 7, "Hotel Lustighof")