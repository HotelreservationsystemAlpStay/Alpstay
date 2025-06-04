from views.StartMenu import StartMenu
from controller.Hotel_Controller import Hotel_Controller
from controller.Room_Controller import RoomController
from controller.RoomType_Controller import RoomType_Controller
from controller.Guest_Controller import Guest_Controller
from controller.Invoice_Controller import Invoice_Controller
from controller.User_Controller import User_Controller
from controller.Booking_Controller import Booking_Controller
from controller.Facility_Controller import Facility_Controller
from controller.Rating_controller import RatingController
class Application:
    def __init__(self):
        self.hotel_Controller = Hotel_Controller()
        self.room_Controller = RoomController()
        self.roomType_Controller = RoomType_Controller()
        self.guest_Controller = Guest_Controller()
        self.invoice_Controller = Invoice_Controller()
        self.user_Controller = User_Controller()
        self.booking_Controller = Booking_Controller()
        self.facility_Controller = Facility_Controller()
        self.rating_Controller = RatingController()
        self.__is_running = True

    def stop(self):
        self.__is_running = False

    def run(self):
        next = StartMenu(self)
        while self.__is_running:
            if next:
                next = next.run()
            else:
                self.stop()
if __name__ == "__main__":
    app = Application()
    app.run()