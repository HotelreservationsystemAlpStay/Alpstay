import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Base_Access_Controller import Base_Access_Controller

class Rating_Access:

    def __init__(self):
        self.db = Base_Access_Controller()

 #3 Als Gast möchte ich vor der Buchung Hotelbewertungen lesen, damit ich das beste Hotel auswählen kann.

    def get_hotel_details(self, hotel_id):

        sql_main = """
        SELECT 
            Hotel.name,
            Hotel.stars,
            Address.street,
            Address.city,
            Address.zip_code
        FROM Hotel
        JOIN Address ON Hotel.address_id = Address.address_id
        WHERE Hotel.hotel_id = ?
        """
        
        sql_facilities = """
        SELECT DISTINCT Facilities.facility_name
        FROM Room
        JOIN Room_Facilities ON Room.room_id = Room_Facilities.room_id
        JOIN Facilities ON Room_Facilities.facility_id = Facilities.facility_id
        WHERE Room.hotel_id = ?
        """
        
        hotel = self.db.fetchone(sql_main, (hotel_id,))
        facilities = self.db.fetchall(sql_facilities, (hotel_id,))
        
        if not hotel:
            print(f"Kein Hotel mit ID {hotel_id} gefunden.")
            return
        
        facility_list = [f['facility_name'] for f in facilities]
        facilities_str = ', '.join(facility_list) if facility_list else 'Keine'
        
        # Test
        print(f"\nHotel-Details (ID: {hotel_id}):")
        print()
        print(f"Name: {hotel['name']}")
        print(f"Sterne: {hotel['stars']}")
        print(f"Adresse: {hotel['street']}, {hotel['zip_code']} {hotel['city']}")
        print(f"Einrichtungen: {facilities_str}")

#if __name__ == "__main__":
    access = Rating_Access()
    access.get_hotel_details(1)
