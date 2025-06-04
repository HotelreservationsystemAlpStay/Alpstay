from models.Facility import Facility
from models.Room_Type import Room_Type

class Room:
    def __init__(self, room_id: int, room_no: str, price_per_night: float, facilities:list[Facility] = None, room_Type:Room_Type = None, hotelid:int=None):
        self._room_id = room_id
        self._room_no = room_no
        self._price_per_night = price_per_night
        self._facilities = facilities if facilities is not None else []
        self._room_Type = room_Type
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
    def room_Type(self) -> Room_Type:
        return self._room_Type

    @room_Type.setter
    def room_Type(self, room_Type: Room_Type) -> None:
        self._room_Type = room_Type

    @property
    def hotelid(self) -> int:
        return self._hotelid

    @hotelid.setter
    def hotelid(self, hotelid: int) -> None:
        self._hotelid = hotelid
    
    def __str__(self):
        return f"Room {self._room_no} costs {self._price_per_night} per night and has room ID: {self._room_id}"

    def extendedStr(self):
        rstr = f"Room {self._room_no} costs {self._price_per_night}, is of type {self.room_Type.description} with max guests of {self.room_Type.maxGuests} per night and has room ID: {self._room_id}"
        rstr += f"\nFacilities"
        for facility in self.facilities:
            rstr += f"\n{facility.name}"
            
        return rstr
    
    def to_dict(self):
        return{
            "room_id": self._room_id,
            "room_no": self._room_no,
            "price_per_night": self._price_per_night,
            "facilities": [f.to_dict() for f in self._facilities] if self._facilities else [],
            "room_Type": self._room_Type.to_dict() if self._room_Type else None,
            "hotelid": self._hotelid
        }