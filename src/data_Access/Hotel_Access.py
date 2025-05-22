import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data_Access.Base_Access_Controller import Base_Access_Controller
from datetime import date
from models.Hotels import Hotel

class Hotel_Access:
    def __init__(self): 
        self.db = Base_Access_Controller()

    def access_hotel_in_city(self, city):
        query = """
        SELECT hotel_id, name, stars
        FROM extended_hotel
        WHERE city = ?
        """
        return self.db.fetchall(query, (city,))
    
    def access_hotel_in_city_stars(self, city, min_stars):
        query = """
        SELECT hotel_id, name, stars
        FROM extended_hotel
        WHERE city = ? 
        AND stars >= ?
        """
        return self.db.fetchall(query, (city, min_stars))

    def access_hotel_in_city_stars_guests(self, city, min_stars, guests):
        query = """
        SELECT hotel_id, name, stars
        FROM extended_hotel_room
        WHERE city = ? 
        AND stars >= ?
        AND max_guests >= ? 
        """
        return self.db.fetchall(query, (city, min_stars, guests))


#User Story 4 müsste eigentlich stars und guests nicht enthalten, habe es trotzdem mal drin gelassen 
    def access_hotel_in_city_booking(self, city, min_stars, guests, check_in_date, check_out_date):
        query = """
        SELECT DISTINCT hotel_id, name, stars
        FROM extended_hotel_room_booking
        WHERE city = ? 
        AND stars >= ?
        AND max_guests >= ?
        AND room_id NOT IN (
        SELECT room_id
        FROM extended_hotel_room_booking
        WHERE (check_in_date BETWEEN ? AND ?)
        OR (check_out_date BETWEEN ? AND ?)
        OR (check_in_date <= ? AND check_out_date >= ?)
        )
        """
        params = (
            city, min_stars, guests,
            check_in_date, check_out_date,
            check_in_date, check_out_date,
            check_in_date, check_out_date
        )
        return self.db.fetchall(query, params)

    def access_selected_filters(self, city, min_stars, guests, check_in_date, check_out_date):
        query = """
        SELECT DISTINCT hotel_id, name, stars, city, street
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
        return self.db.fetchall(query, parameters)


    def access_hotel_details(self, hotel_name):
        query = """
        SELECT DISTINCT hotel_id, name, stars, street, city 
        FROM extended_hotel_room
        WHERE (name) = (?)       
        """
        return self.db.fetchall(query, (hotel_name,))
    
    def access_add_hotel(self, name, stars, address_id):
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
        self.db.execute(query_add_hotel, (result_max + 1, name, stars, address_id))
        return True


    def access_delete_hotel(self, hotel_id):
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
            return False
        else:
            return True

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