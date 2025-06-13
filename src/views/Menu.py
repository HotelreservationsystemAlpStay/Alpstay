class Menu:
    def __init__(self, title, app):
        """Initialize menu with title and application reference."""
        self.title = title
        self.functions_menu = []
        self.app = app
        
    def add_item(self, name, function):
        """Add a menu item with name and corresponding function."""
        self.functions_menu.append((name, function))

    def display(self):
        """Display all available menu options."""
        for number, (name, function) in enumerate(self.functions_menu, 1):
            print(f"{number} - {name}")

    def input(self):
        """Handle user input and execute selected menu function."""
        try:
            choice = int(input("What would you like to do? -> "))
            choice += -1
            action = self.functions_menu[choice]
            function = action[1]
            return function()
        except ValueError:
            print("Invalid input. Please enter a number.")
            return self.input()
        except IndexError:
            print("Invalid choice. Please try again.")
            return self.input()
        
    def run(self):
        """Run the menu loop until terminated."""
        while True:
            self.display()
            result = self.input()
            if result is None:
                break
            elif isinstance(result, Menu):
                result.run()
