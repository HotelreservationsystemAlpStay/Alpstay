from models.Facility import Facility
from models.RoomType import RoomType

class Room:
    def __init__(self, room_id: int, room_no: str, price_per_night: float, facilities:list[Facility] = None, roomType:RoomType = None, hotelid:int=None):
        self._room_id = room_id
        self._room_no = room_no
        self._price_per_night = price_per_night
        self._facilities = facilities if facilities is not None else []
        self._roomType = roomType
        self._hotelid = hotelid

    @property
    def room_id(self) -> int:
        return self._room_id

    @room_id.setter
    def room_id(self, room_id: int) -> None:
        self._room_id = room_id

    @property
    def room_no(self) -> str:
        return self._room_no

    @room_no.setter
    def room_no(self, room_no: str) -> None:
        self._room_no = room_no

    @property
    def price_per_night(self) -> float:
        return self._price_per_night

    @price_per_night.setter
    def price_per_night(self, price_per_night: float) -> None:
        self._price_per_night = price_per_night

    @property
    def facilities(self) -> list[Facility]:
        return self._facilities

    @facilities.setter
    def facilities(self, facilities: list[Facility]) -> None:
        self._facilities = facilities

    @property
    def roomType(self) -> RoomType:
        return self._roomType

    @roomType.setter
    def roomType(self, roomType: RoomType) -> None:
        self._roomType = roomType

    @property
    def hotelid(self) -> int:
        return self._hotelid

    @hotelid.setter
    def hotelid(self, hotelid: int) -> None:
        self._hotelid = hotelid
    
    def __str__(self):
        return f"Room {self._room_no} costs {self._price_per_night} per night and has room ID: {self._room_id}"

    def to_dict(self):
        return{
            "room_id": self._room_id,
            "room_no": self._room_no,
            "price_per_night": self._price_per_night,
            "facilities": [f.to_dict() for f in self._facilities] if self._facilities else [],
            "roomType": self._roomType.to_dict() if self._roomType else None,
            "hotelid": self._hotelid
        }