class Room_Type:
    def __init__(self, id: int, description: str, maxGuests: int) -> None:
        self._id = id
        self._description = description
        self._maxGuests = maxGuests

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        self._id = id

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        self._description = description

    @property
    def maxGuests(self) -> int:
        return self._maxGuests

    @maxGuests.setter
    def maxGuests(self, maxGuests: int) -> None:
        self._maxGuests = maxGuests

    def __str__(self):
        return "RoomType(id={0}, description={1},maxGuests={2})".format(
            self._id, self._description, self._maxGuests
        )

    def to_dict(self):
        return {
            "id": self._id,
            "description": self._description,
            "maxGuests": self._maxGuests,
        }
