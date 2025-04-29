import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from handlers.Service_Handler import ServiceHandler
from datetime import datetime, date

class ConsoleView:
    def __init__(self):
        self.service = ServiceHandler()

    def run(self):
        while True:
            print("\nAlpsty Hotelreservationsystem Console")
            print("1.")
            print("q. Quit")
            choice = input("Select an option: ")
            if choice == '1':
                print("1.")
            elif choice.lower() == 'q':
                print("Exiting.")
                break
            else:
                print("Invalid choice.")