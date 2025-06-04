from views.Menu import Menu
from models.Facility import Facility

class Facility_Menu(Menu):
    def __init__(self, app, prev:Menu):
        super().__init__("Facility Menu", app)
        self._prev_menu = prev
        self.add_item("Get Facilities", self.getFacilities)
        self.add_item("Update Facility", self.updateFacility)
        self.add_item("Back", self.back)
        
    def getFacilities(self, fromFunction=False):
        facilities = self.app.facility_Manager.get_facilities()
        print("-----------")
        counter = 1
        for facility in facilities:
            print(f"{counter}. {facility}")
            counter += 1
        print("-----------")
        if fromFunction:
            return facilities
        return self
    
    def updateFacility(self):
        facilities = self.getFacilities(fromFunction=True)
        choice = int(input("Please enter choice of Facility to update: "))-1
        name = input("Enter new name: ")
        if name == "":
            print("no name provided")
            return self
        facility = facilities[choice]
        facility.name = name
        print(self.app.facility_Manager.update_facility(facility))
        return self
        
    def back(self)->Menu:
        return self._prev_menu