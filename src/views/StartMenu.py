import sys
from views.Menu import Menu
from mythic.mythic_code import Mythic
from views.UserStorymenu import UserStoryMenu

class StartMenu(Menu):
    def __init__(self, app):
        super().__init__("Menu", app)
        self.add_item("User Story Menu", self.link_userstories)
        self.add_item("Quit", self.quit)
        self.add_item("Mythical Stuff", self.mythical_stuff)

    def mythical_stuff(self):
        ms = Mythic()
        ms.wtf()
        return self
    
    def link_userstories(self):
        return UserStoryMenu(self.app, self)
    
    def quit(self):
        print("Everything has an end but the sausage has two")
        print("--------------------------------")
        print("Thank you for using our application")
        print("We hope you enjoyed it!")
        sys.exit()


        
