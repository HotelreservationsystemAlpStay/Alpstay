import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#from controller.Access_Controller import Access_Controller
from datetime import datetime, date

class ConsoleView:
    def __init__(self):
        #self.service = Access_Controller()
        print("ConsoleView initialized")

    def run(self):
        while True:
            print("\nAlpsty Hotelreservationsystem Console")
            print("1. Hello World")
            print("2. Show all guests")
            print("3. Show all rooms")
            print("4. Show all bookings")
            print("q. Quit")
            choice = input("Select an option: ")
            if choice == '1':
                print("1.")
            elif choice == '2':
                print("Showing all guests...")
            elif choice == '3':
                print("Showing all rooms...")
            elif choice == '4':
                print("Showing all bookings...")
            elif choice.lower() == 'q':
                print("Exiting.")
                break
            else:
                print("Invalid choice.")