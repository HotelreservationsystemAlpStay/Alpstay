class Room:
    def __init__(self, room_id: int, room_no: str, price_per_night: float):
        self._validate_room_id(room_id)
        self._validate_room_no(room_no)
        self._validate_price_per_night(price_per_night)

        self._room_id = room_id
        self._room_no = room_no
        self._price_per_night = price_per_night

    def _validate_room_id(self, room_id):
        if not isinstance(room_id, int):
            raise ValueError("Room ID must be an integer")
        if room_id < 1:
            raise ValueError("Room ID must be greater than 0")

    def _validate_room_no(self, room_no):
        if not isinstance(room_no, str):
            raise ValueError("Room number must be a string")
        if room_no.strip() == "":
            raise ValueError("Please enter a room number")

    def _validate_price_per_night(self, price_per_night):
        if not isinstance(price_per_night, (float, int)):
            raise ValueError("Price per night must be a float or integer")
        if price_per_night <= 0:
            raise ValueError("Price per night must be greater than 0")

    @property
    def room_id(self):
        return self._room_id

    @room_id.setter
    def room_id(self, new_room_id):
        self._validate_room_id(new_room_id)
        self._room_id = new_room_id

    @property
    def room_no(self):
        return self._room_no

    @room_no.setter
    def room_no(self, new_room_no):
        self._validate_room_no(new_room_no)
        self._room_no = new_room_no

    @property
    def price_per_night(self):
        return self._price_per_night

    @price_per_night.setter
    def price_per_night(self, new_price_per_night):
        self._validate_price(new_price_per_night)
        self._price_per_night = new_price_per_night

    def __str__(self):
        return f"Room {self._room_no} costs {self._price_per_night} per night and has room ID: {self._room_id}"
