import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.Validator import Validator
from models.Facility import Facility
from data_Access.Base_Access_Controller import Base_Access_Controller
import sqlite3


class Facility_Access:
    def __init__(self):
        self.db = Base_Access_Controller()

    @staticmethod
    def _sqlite3row_to_room(row: sqlite3.Row) -> Facility:
        return Facility(id=row["facility_id"], name=row["facility_name"])

    def get_facility_by_id(self, facility_id: int)->Facility:
        query = "SELECT * FROM Facilities WHERE facility_id = ?"
        results = self.db.fetchone(query, (facility_id,))
        return self._sqlite3row_to_room(results)
    
    def get_room_facilities(self, room_id: int) -> list:
        query = """
        SELECT Facilities.facility_id, Facilities.facility_name
        FROM Facilities
        JOIN Room_Facilities ON Facilities.facility_id = Room_Facilities.facility_id
        WHERE Room_Facilities.room_id = ?
        """
        result = self.db.fetchall(query, (room_id,))
        if not result: 
            return []
        return result
    
if __name__ == "__main__":
    try:
        access = Facility_Access()
        room_id = 1  # Zimmer-ID, die Sie abfragen möchten
        
        print(f"\nAbrufe Ausstattung für Zimmer ID {room_id}...")
        facilities = access.get_room_facilities(room_id)
        
        if not facilities:
            print(f"Keine Ausstattung für Zimmer ID {room_id} gefunden.")
        else:
            print(f"Ausstattung für Zimmer ID {room_id}:")
            for facility in facilities:
                print(f" - ID: {facility['facility_id']}, Name: {facility['facility_name']}")
            print(f"\nGesamtanzahl: {len(facilities)} Einrichtungen")
            
    except Exception as e:
        print(f"Fehler aufgetreten: {str(e)}")
    finally:
        # Datenbankverbindung schließen
        if 'access' in locals():
            access.db.close()





