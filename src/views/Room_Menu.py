from views.Menu import Menu
from models.Hotels import Hotel
from models.Room import Room

class Room_Menu(Menu):
    def __init__(self, app, prev:Menu):
        """Initialize Room Menu with application reference and previous menu."""
        super().__init__(title="Room Menu", app=app)
        self._prev_menu = prev
        self.add_item("Get Rooms", self.get_rooms)
        self.add_item("Update Room", self.update_room)
        self.add_item("Back", self.back)

    def get_rooms(self,fromFunction=False):
        """Display all rooms with extended information.
        
        Args:
            fromFunction (bool): If True, returns room list for other functions
            
        Returns:
            self or list[Room]: Returns self for chaining or room list if fromFunction=True
        """
        rooms = self.app.room_Manager.get_rooms()
        print("------")
        counter = 1
        for room in rooms:
            print(f"{counter}. {room.extendedStr()}")
            counter +=1
        print("------")
        if fromFunction:
            return rooms
        return self
        
    def update_room(self):
        """Allow user to select and update a room's price."""
        rooms = self.get_rooms(fromFunction=True)
        choice = int(input("Please enter choice of Room to update: "))-1
        price = input("Enter new price: ")
        if price == "":
            print("No price provided")
        price = float(price)
        room = rooms[choice]
        room.price_per_night = price
        room = self.app.room_Manager.update_room(room)
        print(room)
        return self
    
            
    def back(self)->Menu:
        """Return to the previous menu."""
        return self._prev_menu