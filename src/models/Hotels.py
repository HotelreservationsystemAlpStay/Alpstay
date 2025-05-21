from models.Room import Room
from models.Address import Address

class Hotel:
    def __init__(self, hotel_id: int, name: str, stars: int, rooms:list[Room]=None, address:Address=None):
        self._validate_hotel_id(hotel_id)
        self._validate_name(name)
        self._validate_stars(stars)

        self._hotel_id = hotel_id
        self._name = name
        self._stars = stars
        self.rooms = rooms
        self.address = address

    def _validate_hotel_id(self, hotel_id):
        if not isinstance(hotel_id, int):
            raise ValueError("Hotel ID must be an integer")
        if hotel_id < 1:
            raise ValueError("Hotel ID cannot be negative")

    def _validate_name(self, name):
        if not isinstance(name, str):
            raise ValueError("Hotel name must be a string")
        if name.strip() == "":
            raise ValueError("Please enter a hotel name")

    def _validate_stars(self, stars):
        if not isinstance(stars, int):
            raise ValueError("Hotel stars must be an integer")
        if stars < 1 or stars > 5:
            raise ValueError("Hotel stars must be between 1 and 5")

    @property
    def hotel_id(self):
        return self._hotel_id

    @hotel_id.setter
    def hotel_id(self, new_hotel_id: int):
        self._validate_hotel_id(new_hotel_id)
        self._hotel_id = new_hotel_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        self._validate_name(new_name)
        self._name = new_name

    @property
    def stars(self):
        return self._stars

    @stars.setter
    def stars(self, new_stars: int):
        self._validate_stars(new_stars)
        self._stars = new_stars

    def __str__(self):
        return f"Hotel {self._name} has {self._stars} stars and hotel ID {self._hotel_id}"
