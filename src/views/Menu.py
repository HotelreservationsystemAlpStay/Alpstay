class Menu:
    def __init__(self, title, app):
        self.title = title
        self.functions_menu = []
        self.app = app
    def add_item(self, name, function):
        self.functions_menu.append((name, function))
    def display(self):
        for number, (name, function) in enumerate(self.functions_menu, 1):
            print(f"{number} - {name}")
    def input(self):
        choice = int(input("What would you like to do? -> "))
        choice += -1
        action = self.functions_menu[choice]
        function = action[1]
        return function()
    def run(self):
        while True:
            self.display()
            result = self.input()
            if result is None:
                break
            elif isinstance(result, Menu):
                result.run()
