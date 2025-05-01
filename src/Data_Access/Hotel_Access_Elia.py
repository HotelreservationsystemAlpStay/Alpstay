import os  # Importiert Betriebssystemoperationen
import sys  # Importiert Systemoperationen (z.B. um den Pfad zu ändern)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Base_Access_Controller import Base_Access_Controller
from models.Hotels import Hotel


# Variante 2
# Task 1: Alle Hotels anzeigen
# DB bzw. HotelService importieren (das muss pro Datei nur einmal gemacht werden (ausser die Daten sind wo anders gespeichert))
# DB controller hinzufügen (Kommunikation von Python mit DB)
# Hier kann man die richtige Tabelle importieren, auf die man zugreifen möchte
# Python Pfad hinzufügen für die Importierung


# Klasse/Tabelle auswählen bzw. Klasse definieren (die kommenden Ausgaben bzw. gewünschten Daten müssen in dieser Klasse vorkommen, sonst muss man eine neue Klasse öffnen bzw. laden)


class Hotel_Access:
    def __init__(self):  # Konstruktor der Klasse -> Definition Konstruktor: Dient dazu, Instanzattribute (Variable, die einer Instanz einer Klasse angehört) zu initialisieren und aktionen beim Erzeugen eines Objekts durchzuführen
        # Datenbankcontroller wird aufgerufen, um die Datenbank zu steuern
        self.db = Base_Access_Controller()

    # Alle Hotels anzeigen:
    def get_hotels(self):  # Definiert die Methode, wie man die Hotels anzeigen lassen will bzw. wie man diese nennt und was sie anzeigen soll (hier mit eimem get_hotels)
        query = """ SELECT hotel_id, name, stars FROM extended_hotel """  # SQL Abfrage
        result = self.db.fetchall(
            query)  # Führt die SQL Abfrage aus und speichert die Werte/Ergebnisse in "result"
        if not result:  # Kontrolliert, ob überhaupt etwas vorhanden ist oder ob die DB leer ist
            print("No hotels found")
        else:
            print("List of all hotels:")
            hotels = []  # Erstellt eine leere Liste, die anschliessend gefüllt wird
            for row in result:  # Ergebniszeilen der SQL Abfrage
                # Wandelt die Daten in ein Dictionary (Variabeln speichern) um
                data = dict(row)
                hotel = Hotel(  # Neues Objekt wird erstellt und sammelt in den folgenden Schritten die gewünschten Daten
                    hotel_id=data["hotel_id"],  # Hotel ID aus DB holen
                    name=data["name"],  # Name aus DB holen
                    stars=data["stars"]  # Sterne aus DB holen
                )
                hotels.append(hotel)  # Fügt das Hotel-Objekt der Liste hinzu
            for hotel in hotels:
                # Endausgabe
                print(f"Hotel: {hotel.name}, Stars: {hotel.stars}")

    # User Story 1:
    def get_hotel_in_city(self, city, stars):
        query = """ SELECT hotel_id, name, stars FROM extended_hotel WHERE city = ? """  # SQL Abfrage, die nach Stadt filtert
        result = self.db.fetchall(query, (city, stars))
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
            # Endausgabe
            print(f"{hotel.name} has {hotel.stars} stars and is located in {city}")


hotels = Hotel_Access()  # Erstellt eine Instanz (Objekt) der Hotelservice Klasse
hotels.get_hotels()  # Ruft die get_hotels auf
hotels.get_hotel_in_city("Luzern", 3)  # Ruft die get_hotel_in_city auf
