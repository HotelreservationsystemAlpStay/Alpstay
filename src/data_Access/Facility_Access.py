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
    def _sqlite3row_to_facility(row: sqlite3.Row) -> Facility:
        """generates an object of type facility based on sqlite3row

        Args:
            row (sqlite3.Row): row from databse

        Returns:
            Facility: translated object
        """
        return Facility(id=row["facility_id"], name=row["facility_name"])

    def get_facilities(self)->list[Facility]:
        """returns list of facilities

        Returns:
            list[Facility]: list of facilities
        """
        query = "SELECT * FROM Facilities"
        result = self.db.fetchall(query=query)
        facilities = []
        for row in result:
            facilities.append(self._sqlite3row_to_facility(row))
        return facilities

    def get_facility_by_id(self, facility_id: int)->Facility:
        """returns facility of provided id

        Args:
            facility_id (int): facility id as is in db

        Returns:
            Facility: translated object
        """
        query = "SELECT * FROM Facilities WHERE facility_id = ?"
        results = self.db.fetchone(query, (facility_id,))
        return self._sqlite3row_to_facility(results)
    
    def update_facility(self, facility: Facility) -> Facility:
        """updates facility in db to object provided, return updated and newly loaded facility to may check whether everything has been done correctly

        Args:
            facility (Facility): object to be saved in db

        Returns:
            Facility: updated row in db to translated object
        """
        query = "UPDATE Facilities SET facility_name = ? WHERE facility_id = ?"
        self.db.execute(query=query, params=(facility.name,facility.id))
        return self.get_facility_by_id(facility_id=facility.id)
    
    def get_room_facilities(self, room_id: int) -> list[Facility]:
        """return list of facilities which are connected to provided room id
        
        Args:
            room_id (int): room id
            
        Return:
            list[Facility]: list of associated facilities
        """
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





