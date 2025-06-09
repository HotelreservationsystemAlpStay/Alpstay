from views.Menu import Menu
from models.Room_Type import Room_Type

class Room_Type_Menu(Menu):
    def __init__(self, app, prev: Menu):
        super().__init__("Room_Type Menu", app=app)
        self._prev_menu = prev
        self.add_item("Get Room_Types", self.getroom_Types)
        self.add_item("Update Room_Type", self.updateRoomType)
        self.add_item("Back", self.back)
        
    def getroom_Types(self, fromFunction = False):
        room_Types = self.app.roomType_Manager.get_all_roomtypes()
        counter = 1
        print("---------")
        for roomType in room_Types:
            print(f"{counter}. {roomType}")
            counter += 1
        print("---------")
        if fromFunction:
            return room_Types
        return self
    
    def updateRoomType(self):
        room_Types = self.getroom_Types(fromFunction=True)
        choice = int(input("Please enter choice of RoomType to update: "))-1
        description = input("Decription - hit enter to leave it as is: ")
        maxGuests = input("Max Guests - hit enter to leave it as is: ")
        if maxGuests == "": 
            maxGuests = None
        else:
            maxGuests = int(maxGuests)
        if description == "":
            description = None
        self.app.roomType_Manager.modify_roomType(room_Types[choice], description, maxGuests)
        print(self.app.roomType_Manager.get_roomType_by_id(room_Types[choice].id))
        return self
    
    def back(self):
        return self._prev_menu