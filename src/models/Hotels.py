from models.Room import Room
from models.Address import Address

class Hotel:
    def __init__(self, hotel_id: int, name: str, stars: int, rooms:list[Room]=None, address:Address=None):
        """Initialize a Hotel with id, name, stars, and optional rooms and address."""
        self._hotel_id = hotel_id
        self._name = name
        self._stars = stars
        self._rooms = rooms if rooms is not None else []
        self._address = address

    @property
    def hotel_id(self) -> int:
        """Get the hotel ID."""
        return self._hotel_id

    @hotel_id.setter
    def hotel_id(self, new_hotel_id: int) -> None:
        """Set the hotel ID."""
        self._hotel_id = new_hotel_id

    @property
    def name(self) -> str:
        """Get the hotel name."""
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Set the hotel name."""
        self._name = new_name

    @property
    def stars(self) -> int:
        """Get the hotel star rating."""
        return self._stars

    @stars.setter
    def stars(self, new_stars: int) -> None:
        """Set the hotel star rating."""
        self._stars = new_stars

    @property
    def rooms(self) -> list[Room]:
        """Get the list of hotel rooms."""
        return self._rooms

    @rooms.setter
    def rooms(self, new_rooms: list[Room]) -> None:
        """Set the list of hotel rooms."""
        self._rooms = new_rooms

    @property
    def address(self) -> Address:
        """Get the hotel address."""
        return self._address

    @address.setter
    def address(self, new_address: Address) -> None:
        """Set the hotel address."""
        self._address = new_address

    def __str__(self):
        """Return string representation of the hotel."""
        return f"Hotel {self._name} has {self._stars} stars and hotel ID {self._hotel_id}"

    def to_dict(self) -> dict:
        """Convert hotel to dictionary format."""
        return {
            'hotel_id': self._hotel_id,
            'name': self._name,
            'stars': self._stars,
            'rooms': [room.to_dict() for room in self._rooms] if self._rooms else [],
            'address': self._address.to_dict() if self._address else None
        }
