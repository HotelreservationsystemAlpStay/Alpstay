from data_Access.Facility_Access import Facility_Access
from models.Facility import Facility

class Facility_Manager:
    def __init__(self):
        self.facilityAccess = Facility_Access()
    
    def get_facilities(self) -> list[Facility]:
        """returns list of facilities

        Returns:
            list[Facility]: list of facilities
        """
        return self.facilityAccess.get_facilities()
    
    def get_facility_by_id(self, id:int)->Facility:
        """returns facility of provided id

        Args:
            facility_id (int): facility id as is in db

        Returns:
            Facility: translated object
        """
        return self.facilityAccess.get_facility_by_id(facility_id=id)
    
    def update_facility(self, facility:Facility) -> Facility:
        """updates facility in db to object provided, return updated and newly loaded facility to may check whether everything has been done correctly

        Args:
            facility (Facility): object to be saved in db

        Returns:
            Facility: updated row in db to translated object
        """
        return self.facilityAccess.update_facility(facility)