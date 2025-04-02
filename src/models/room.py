class Room:
    def __init__(self, room_id: int, room_no: str, price_per_night: float):
        if not isinstance(room_id, int):
            raise ValueError("Die Room-ID muss eine Integer sein")
        if not isinstance(room_no, str):
            raise ValueError("Die Zimmernummer muss ein String sein")
        if not isinstance(price_per_night, (float, int)):
            raise ValueError("Der Preis pro nacht muss ein Float sein")
        if room_id <1:
            raise ValueError("Die Room-ID muss grösser als 0 sein")
        if room_no.strip() == "":
            raise ValueError("Bitte gib eine Zimmernummer ein")
        if price_per_night <=0:
            raise ValueError("Der Preis pro Nacht muss grösser als 0 sein")
        self._room_id = room_id
        self._room_no = room_no
        self._price_per_night = price_per_night
    @property
    def room_id(self):
        return self._room_id
    #Wollen wir wirklich setter für IDs?
    @room_id.setter
    def room_id(self, new_room_id):
        if not isinstance(new_room_id, int):
            raise ValueError("Die neue Room-ID muss eine Integer sein")
        if new_room_id <1:
            raise ValueError("Die neue Room-ID muss grösser als 0 sein")
        self._room_id = new_room_id
    @property
    def room_no(self):
        return self._room_no
    @room_no.setter
    def room_no(self, new_room_no):
        if not isinstance(new_room_no, str):
            raise ValueError("Die neue Zimmernummer muss ein String sein")
        if new_room_no.strip() == "":
            raise ValueError("Bitte gib eine neue Zimmernummer ein")
        self._room_no = new_room_no
    @property
    def price_per_night(self):
        return self._price_per_night
    @price_per_night.setter
    def price_per_night(self, new_price_per_night):
        if not isinstance(new_price_per_night, (float, int)):
            raise ValueError("Der neue Preis pro Nacht muss ein Float sein")
        if new_price_per_night <=0:
            raise ValueError("Der neue Preis pro Nacht muss grösser als 0 sein")
        self._price_per_night = new_price_per_night