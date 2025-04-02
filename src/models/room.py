class Room:
    def __init__(self, room_id: int, room_no: str, price_per_night: float):
        self._room_id = room_id
        self._room_no = room_no
        self._price_per_night = price_per_night
    @property
    def room_id(self):
        return self._room_id
    #Wollen wir wirklich setter für IDs?
    @room_id.setter
    def room_id(self, new_room_id):
        self._room_id = new_room_id
    @property
    def room_no(self):
        return self._room_no
    @room_no.setter
    def room_no(self, new_room_no):
        self._room_no = new_room_no
    @property
    def price_per_night(self):
        return self._price_per_night
    @price_per_night.setter
    def price_per_night(self, new_price_per_night):
        self._price_per_night = new_price_per_night