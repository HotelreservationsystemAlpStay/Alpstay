class RoomType:
    def __init__(self, id: int, description: str, maxGuests: int) -> None:
        self._validateId(id)
        self._validateDescription(description)
        self._validateMaxGuests(maxGuests)

        self.id = id
        self.description = description
        self.maxGuests = maxGuests

    def _validateId(self, id: int) -> None:
        if not isinstance(id, int):
            raise TypeError("ID must be an integer")
        if id <= 0:
            raise ValueError("ID must be positive")

    def _validateDescription(self, description: str) -> None:
        if not isinstance(description, str):
            raise TypeError("Description must be a String")
        if not description.strip():
            raise ValueError("Description must not be empty")

    def _validateMaxGuests(self, maxGuests: int) -> None:
        if not isinstance(maxGuests, int):
            raise TypeError("Maximum count of guests must be an integer")
        if maxGuests <= 0:
            raise ValueError("Maximum count of guests must be positive")

    @property
    def getId(self) -> int:
        return self.id

    @getId.setter
    def setId(self, id: int) -> None:
        self.id = id

    @property
    def getDescription(self) -> str:
        return self.description

    @getDescription.setter
    def setDescription(self, description: str) -> None:
        self.description = description

    @property
    def getMaxGuests(self) -> int:
        return self.maxGuests

    @getMaxGuests.setter
    def setMaxGuests(self, maxGuests: int) -> None:
        self.maxGuests = maxGuests

