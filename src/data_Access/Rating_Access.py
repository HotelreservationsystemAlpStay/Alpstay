import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Base_Access_Controller import Base_Access_Controller

class Rating_Access:

    def __init__(self):
        self.db = Base_Access_Controller()

 #3 Als Gast möchte ich vor der Buchung Hotelbewertungen lesen, damit ich das beste Hotel auswählen kann.

    def get_hotel_ratings(self, hotel_id):

        sql = """
        SELECT 
        Rating.rating, Rating.comment, Guest.first_name || ' ' || Guest.last_name AS guest_name, Rating.created_at
        FROM Rating
        JOIN Guest ON Rating.guest_id = Guest.guest_id
        WHERE Rating.hotel_id = ?
        ORDER BY Rating.created_at DESC 
        """
        ratings = self.db.fetchall(sql, (hotel_id,))

        if not ratings: 
            print(f"Keine Bewertung für Hotel ID {hotel_id} gefunden.")
            return
        print(f"\nBewertungen für Hotel ID {hotel_id}:")
        for rating in ratings:
            print(f"\n{rating['rating']}/5")
            print(f"{rating['comment']}")
            print(f"{rating['guest_name']}")
            print(f"{rating['created_at'].split()[0]}")

if __name__ == "__main__":
    access = Rating_Access()
    
    #Abfrage:

    print("Testabfrage für Hotel ID 1")
    access.get_hotel_ratings(1)