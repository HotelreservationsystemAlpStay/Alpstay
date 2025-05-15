from views.StartMenu import StartMenu
from controller.Hotel_Controller import Hotel_Controller

class Application:
    def __init__(self):
        self.hotel_Controller = Hotel_Controller()
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