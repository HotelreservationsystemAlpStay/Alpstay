import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from views.StartMenu import StartMenu

if __name__ == "__main__":
    StartMenu().run()