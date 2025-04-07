class RoomType:
    def __init__(self, id: int, description: str, maxGuests: int) -> None:
        self._validateId(id)
        self._validateDescription(description)
        self._validateMaxGuests(maxGuests)
        
        self._id = id
        self._description = description
        self._maxGuests = maxGuests

    def _validateId(self, id: int) -> None:
        if not isinstance(id, int):
            raise TypeError("ID muss eine Ganzzahl sein")
        if id <= 0:
            raise ValueError("ID muss positiv sein")

    def _validateDescription(self, description: str) -> None:
        if not isinstance(description, str):
            raise TypeError("Beschreibung muss ein String sein")
        if not description.strip():
            raise ValueError("Beschreibung darf nicht leer sein")

    def _validateMaxGuests(self, maxGuests: int) -> None:
        if not isinstance(maxGuests, int):
            raise TypeError("Maximale Gästeanzahl muss eine Ganzzahl sein")
        if maxGuests <= 0:
            raise ValueError("Maximale Gästeanzahl muss positiv sein")

    @property
    def getId(self) -> int:
        return self._id

    @getId.setter
    def setId(self, id: int) -> None:
        self._id = id

    @property
    def getDescription(self) -> str:
        return self._description

    @getDescription.setter
    def setDescription(self, description: str) -> None:
        self._description = description

    @property
    def getMaxGuests(self) -> int:
        return self._maxGuests

    @getMaxGuests.setter
    def setMaxGuests(self, maxGuests: int) -> None:
        self._maxGuests = maxGuests
