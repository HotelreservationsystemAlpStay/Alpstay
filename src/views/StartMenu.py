import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from views.MenuView import Menu
from mythic.mythic_code import Mythic
from views.HotelMenu import HotelMenu
class StartMenu(Menu):
    def __init__(self):
        super().__init__("Menu")
        self.add_item("Hotel Menu", self.link_hotel_menu)
        self.add_item("Quit", self.quit)
        self.add_item("Mythical Stuff", self.mythical_stuff)
    def link_hotel_menu(self):
        return HotelMenu()
    def mythical_stuff(self):
        ms = Mythic()
        ms.wtf()
        return self
    def quit(self):
        print("Everything has an end but the sausage has two")
        sys.exit()


        
