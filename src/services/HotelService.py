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
            


        
    
# get_hotels_with_filtercriteria(inquery=[stars],values=[5])
# get_hotels_with_filtercriteria(inquery=[number_of_guests],values=[3])
# get_hotels_with_filtercriteria(inquery=[stars, number_of_guests],values=[5, 3])
# get_hotels_with_filtercriteria(inquery=[dateRange],values=[[date1, date2]])
# get_hotels_with_filtercriteria(inquery=[dateRange, ort] values=[[date1, date2], "Bonstette"])
    def get_hotels_with_filtercriteria(self, inquery = [], values=[]):
        hasAQuery = False
        query = "Select irgwas"
        if len(inquery) == len(values):
            if hasAQuery:
                query += " AND "
            if inquery.containns("stars"):
                index = inquery.index("star")
                query += f"where hotel.stars >= {index}"
            
                

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
story4.get_hotel_in_city_booking("Zürich", 3, 1, "2026-05-05", "2026-06-06")
#Nutzung User Story 5
story5 = Hotelservice()
story5.get_selected_filters("all",3,"all", "all", "all")

#Nutzung User Story 6
story6 = Hotelservice()
story6.get_hotel_details("Hotel Baur au Lac")