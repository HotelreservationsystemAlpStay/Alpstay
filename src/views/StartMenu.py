import sys
from views.Menu import Menu
from mythic.mythic_code import Mythic
from views.UserStorymenu import UserStoryMenu
import random

class StartMenu(Menu):
    def __init__(self, app):
        """Initialize the start menu with application reference."""
        super().__init__("Menu", app)
        self.add_item("User Story Menu", self.link_userstories)
        self.add_item("Quit", self.quit)
        self.add_item("Mythical Stuff", self.mythical_stuff)

    def mythical_stuff(self):
        """Display mythical content."""
        ms = Mythic()
        ms.wtf()
        return self
    
    def link_userstories(self):
        """Navigate to the user story menu."""
        return UserStoryMenu(self.app, self)
    
    def quit(self):
        """Exit the application with a fun message."""
        nubmer = random.randint(1, 2)
        if nubmer == 1:
            print("Everything has an end but the sausage has two")
        else:
            print("Thanks for checking out, we hope your stay was less buggy than our code!")
        sys.exit()



