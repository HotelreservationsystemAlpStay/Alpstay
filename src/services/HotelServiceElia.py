#for testing purposes only !

"""
#Variante 1
#Task 1: Alle Hotels anzeigen
#DB bzw. HotelService importieren
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.HotelService import Hotelservice 

def show_all_hotels():
    hotel_service = Hotelservice()

    hotels = hotel_service.get_hotels() #mit einem get nach Hotels suchen

    if not hotels: #falls keine Hotels vorhanden oder gefunden werden können
        print("No hotels found")  
    else:
        print("List of all hotels:")
        for hotel in hotels:
            print(f"Hotel: {hotel.name}, Stars: {hotel.stars}")


if __name__ == "__main__":
    show_all_hotels()

"""


#Variante 2
#Task 1: Alle Hotels anzeigen
#DB bzw. HotelService importieren (das muss pro Datei nur einmal gemacht werden (ausser die Daten sind wo anders gespeichert))
import sys #Importiert Systemoperationen (z.B. um den Pfad zu ändern)
import os #Importiert Betriebssystemoperationen
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #Python Pfad hinzufügen für die Importierung
from models.Hotels import Hotel #Hier kann man die richtige Tabelle importieren, auf die man zugreifen möchte
from controller.DataBaseController import DataBaseController #DB controller hinzufügen (Kommunikation von Python mit DB)


class Hotelservice: #Klasse/Tabelle auswählen bzw. Klasse definieren (die kommenden Ausgaben bzw. gewünschten Daten müssen in dieser Klasse vorkommen, sonst muss man eine neue Klasse öffnen bzw. laden)
    def __init__(self):  #Konstruktor der Klasse -> Definition Konstruktor: Dient dazu, Instanzattribute (Variable, die einer Instanz einer Klasse angehört) zu initialisieren und aktionen beim Erzeugen eines Objekts durchzuführen
        self.db = DataBaseController() #Datenbankcontroller wird aufgerufen, um die Datenbank zu steuern

    #Alle Hotels anzeigen:
    def get_hotels(self): #Definiert die Methode, wie man die Hotels anzeigen lassen will bzw. wie man diese nennt und was sie anzeigen soll (hier mit eimem get_hotels)
        query = """ SELECT hotel_id, name, stars FROM extended_hotel """ #SQL Abfrage
        result = self.db.fetchall(query) #Führt die SQL Abfrage aus und speichert die Werte/Ergebnisse in "result"
        if not result: #Kontrolliert, ob überhaupt etwas vorhanden ist oder ob die DB leer ist
            print("No hotels found")
        else:
            print("List of all hotels:")
            hotels = [] #Erstellt eine leere Liste, die anschliessend gefüllt wird
            for row in result: #Ergebniszeilen der SQL Abfrage
                data = dict(row) #Wandelt die Daten in ein Dictionary (Variabeln speichern) um
                hotel = Hotel( #Neues Objekt wird erstellt und sammelt in den folgenden Schritten die gewünschten Daten
                    hotel_id=data["hotel_id"], #Hotel ID aus DB holen
                    name=data["name"], #Name aus DB holen
                    stars=data["stars"] #Sterne aus DB holen
                )
                hotels.append(hotel) #Fügt das Hotel-Objekt der Liste hinzu
            for hotel in hotels:
                print(f"Hotel: {hotel.name}, Stars: {hotel.stars}") #Endausgabe

    #User Story 1:
    def get_hotel_in_city(self, city):
        query = """ SELECT hotel_id, name, stars FROM extended_hotel WHERE city = ? """ #SQL Abfrage, die nach Stadt filtert
        result = self.db.fetchall(query, (city,))
        hotels = []
        for row in result:
            data = dict(row)
            hotel = Hotel( 
                hotel_id=data["hotel_id"], 
                name=data["name"],
                stars=data["stars"]
            )
            hotels.append(hotel)
        for hotel in hotels:
            print(f"{hotel.name} has {hotel.stars} stars and is located in {city}") #Endausgabe 

hotels = Hotelservice() #Erstellt eine Instanz (Objekt) der Hotelservice Klasse 
hotels.get_hotels() #Ruft die get_hotels auf
hotels.get_hotel_in_city("Luzern") #Ruft die get_hotel_in_city auf 
