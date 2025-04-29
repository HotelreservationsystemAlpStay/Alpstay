import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from controller.Validator import Validator
from models.Facility import Facility
from controller.DataBaseController import DataBaseController
import sqlite3


class FacilityService:
    def __init__(self):
        self.db = DataBaseController()

    @staticmethod
    def _sqlite3row_to_room(row: sqlite3.Row) -> Facility:
        return Facility(id=row["facility_id"], name=row["facility_name"])

    def get_facility_by_id(self, facility_id: int)->Facility:
        query = "SELECT * FROM Facilities WHERE facility_id = ?"
        results = self.db.fetchone(query, (facility_id,))
        return self._sqlite3row_to_room(results)
        

        
        
        
        