from models.Room import Room
from models.Address import Address

class Hotel:
    def __init__(self, hotel_id: int, name: str, stars: int, rooms:list[Room]=None, address:Address=None):
        self._hotel_id = hotel_id
        self._name = name
        self._stars = stars
        self._rooms = rooms if rooms is not None else []
        self._address = address

    @property
    def hotel_id(self) -> int:
        return self._hotel_id

    @hotel_id.setter
    def hotel_id(self, new_hotel_id: int) -> None:
        self._hotel_id = new_hotel_id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        self._name = new_name

    @property
    def stars(self) -> int:
        return self._stars

    @stars.setter
    def stars(self, new_stars: int) -> None:
        self._stars = new_stars

    @property
    def rooms(self) -> list[Room]:
        return self._rooms

    @rooms.setter
    def rooms(self, new_rooms: list[Room]) -> None:
        self._rooms = new_rooms

    @property
    def address(self) -> Address:
        return self._address

    @address.setter
    def address(self, new_address: Address) -> None:
        self._address = new_address

    def __str__(self):
        return f"Hotel {self._name} has {self._stars} stars and hotel ID {self._hotel_id}"

    def to_dict(self) -> dict:
        return {
            'hotel_id': self._hotel_id,
            'name': self._name,
            'stars': self._stars,
            'rooms': [room.to_dict() for room in self._rooms] if self._rooms else [],
            'address': self._address.to_dict() if self._address else None
        }
