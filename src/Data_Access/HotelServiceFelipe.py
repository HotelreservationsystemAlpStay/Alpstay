import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Data_Access.Base_Access_Controller import Base_Access_Controller

class HotelService:
    def __init__(self):
        self.db = Base_Access_Controller()

#1 Alle Hotels anzeigen
    def get_all_hotels(self):
        sql = "SELECT name FROM Hotel"

        hotels = self.db.fetchall(sql)

        for Hotel in hotels:
            print(Hotel["name"])

# 1.1 Hotel nach Stadt anzeigen lassen

    def search_hotels_by_city(self, city):
        sql = """
        SELECT Hotel.name 
        FROM Hotel 
        JOIN Address ON Hotel.address_id = Address.address_id 
        WHERE Address.city = ?
        """
        hotels = self.db.fetchall(sql, (city,))

        if not hotels:
            print(f"Keine Hotels in '{city}' gefunden.")
        else:
            for hotel in hotels:
                print(hotel["name"])

# 1.2 Hotel nach Sterne anzeigen lassen

    def search_hotels_by_city_and_stars(self, city, stars):
        sql = """
        SELECT Hotel.name, Hotel.stars 
        FROM Hotel 
        JOIN Address ON Hotel.address_id = Address.address_id
        WHERE Address.city = ?
        AND Hotel.stars >= ?
        """
        hotels = self.db.fetchall(sql, (city, stars,))

        if not hotels:
            print(f"Keine Hotels in '{city}' mit mindestens '{stars}' Sternen gefunden.")
        else:
            print(f"\nHotels in {city} mit mindestens {stars} Sternen:")
            for hotel in hotels:
                print(f"{hotel['name']} - {hotel['stars']} Sterne")

# 1.3 Hotels mit Zimmer für bestimmte Anzahl Gäste anzeigen lassen

    def search_hotels_by_city_and_max_guests(self, city, max_guests):
        sql ="""
        SELECT DISTINCT Hotel.name, Room_Type.max_guests
        FROM Hotel
        JOIN Address ON Hotel.address_id = Address.address_id
        JOIN Room ON Hotel.hotel_id = Room.hotel_id
        JOIN Room_Type ON Room.type_id = Room_Type.type_id
        WHERE Address.city = ?
        AND Room_Type.max_guests >= ?
        """
        hotels = self.db.fetchall(sql, (city, max_guests,))

        if not hotels:
            print(f"Keine Hotels in {city} mit Zimmer für {max_guests} Gäste gefunden.")
        else: 
            print(f"\nHotels in {city} mit mindestens {max_guests} Gäste:")
            for hotel in hotels:
                print(f"{hotel['name']} - {hotel['max_guests']} Gäste")

# Abrufe:

if __name__ == "__main__":
    service = HotelService()

    # Alle Hotels
    print("\n=== Alle Hotels ===")
    service.get_all_hotels()

    # Hotels in Bern
    print("\n=== Hotels in Bern ===")
    service.search_hotels_by_city("Bern")

    # 4-Sterne-Hotels in Zürich
    print("\n=== 4-Sterne Hotels in Zürich ===")
    service.search_hotels_by_city_and_stars("Zürich", 4)

    # Hotels für 5+ Gäste
    print("\n=== Hotels in Zürich für 5+ Gäste ===")
    service.search_hotels_by_city_and_max_guests("Zürich", 5)
