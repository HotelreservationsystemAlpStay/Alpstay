class Room_Type:
    def __init__(self, id: int, description: str, maxGuests: int) -> None:
        """Initialize a Room Type with id, description, and maximum guests."""
        self._id = id
        self._description = description
        self._maxGuests = maxGuests

    @property
    def id(self) -> int:
        """Get the room type ID."""
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        """Set the room type ID."""
        self._id = id

    @property
    def description(self) -> str:
        """Get the room type description."""
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """Set the room type description."""
        self._description = description

    @property
    def maxGuests(self) -> int:
        """Get the maximum number of guests."""
        return self._maxGuests

    @maxGuests.setter
    def maxGuests(self, maxGuests: int) -> None:
        """Set the maximum number of guests."""
        self._maxGuests = maxGuests

    def __str__(self):
        """Return string representation of the room type."""
        return "RoomType(id={0}, description={1},maxGuests={2})".format(
            self._id, self._description, self._maxGuests
        )

    def to_dict(self):
        """Convert room type to dictionary format."""
        return {
            "id": self._id,
            "description": self._description,
            "maxGuests": self._maxGuests,
        }
