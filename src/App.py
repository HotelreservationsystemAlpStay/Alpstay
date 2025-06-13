from views.StartMenu import StartMenu
from managers.Hotel_Manager import Hotel_Manager
from managers.Room_Manager import Room_Manager
from managers.Room_Type_Manager import Room_Type_Manager
from managers.Guest_Manager import Guest_Manager
from managers.Invoice_Manager import Invoice_Manager
from managers.User_Manager import User_Manager
from managers.Booking_Manager import Booking_Manager
from managers.Facility_Manager import Facility_Manager
from managers.Rating_Manager import RatingManager
class Application:
    def __init__(self):
        """Initialize the application with all necessary managers."""
        self.hotel_Manager = Hotel_Manager()
        self.room_Manager = Room_Manager()
        self.roomType_Manager = Room_Type_Manager()
        self.guest_Manager = Guest_Manager()
        self.invoice_Manager = Invoice_Manager()
        self.user_Manager = User_Manager()
        self.booking_Manager = Booking_Manager()
        self.facility_Manager = Facility_Manager()
        self.rating_Manager = RatingManager()
        self.__is_running = True

    def stop(self):
        """Stop the application by setting the running flag to False."""
        self.__is_running = False

    def run(self):
        """Run the main application loop."""
        next = StartMenu(self)
        while self.__is_running:
            if next:
                next = next.run()
            else:
                self.stop()
if __name__ == "__main__":
    app = Application()
    app.run()