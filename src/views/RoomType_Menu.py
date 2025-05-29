from views.Menu import Menu
from models.RoomType import RoomType

class RoomType_Menu(Menu):
    def __init__(self, app, prev: Menu):
        super().__init__("RoomType Menu", app=app)
        self._prev_menu = prev
        self.add_item("Get RoomTypes", self.getRoomTypes)
        self.add_item("Update RoomType", self.updateRoomType)
        self.add_item("Back", self.back)
        
    def getRoomTypes(self, fromFunction = False):
        roomTypes = self.app.roomType_Controller.get_all_roomtypes()
        counter = 1
        print("---------")
        for roomType in roomTypes:
            print(f"{counter}. {roomType}")
        print("---------")
        if fromFunction:
            return roomTypes
        return self
    
    def updateRoomType(self):
        roomTypes = self.getRoomTypes(fromFunction=True)
        choice = int(input("Please enter choice of RoomType to update: "))-1
        description = input("Decription - hit enter to leave it as is: ")
        maxGuests = input("Max Guests - hit enter to leave it as is: ")
        if maxGuests == "": 
            maxGuests = None
        else:
            maxGuests = int(maxGuests)
        if description == "":
            description = None
        self.app.roomType_Controller.modify_roomType(roomTypes[choice], description, maxGuests)
        print(self.app.roomType_Controller.get_roomType_by_id(roomTypes[choice].id))
        return self
    
    def back(self):
        return self._prev_menu