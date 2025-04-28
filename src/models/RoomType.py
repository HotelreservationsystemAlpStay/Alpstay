import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from controller.Validator import Validator

class RoomType:
    def __init__(self, id: int, description: str, maxGuests: int) -> None:
        self.validator = Validator()
        self.validator.checkID(id)
        self.validator.checkStr(description, "description")
        self.validator.checkPositiveInteger(maxGuests, "maxGuest")

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
        self.validator.checkID(id)
        self.id = id

    @property
    def getDescription(self) -> str:
        return self.description

    @getDescription.setter
    def setDescription(self, description: str) -> None:
        self._validateDescription(description)
        self.description = description

    @property
    def getMaxGuests(self) -> int:
        return self.maxGuests

    @getMaxGuests.setter
    def setMaxGuests(self, maxGuests: int) -> None:
        self._validateMaxGuests(maxGuests)
        self.maxGuests = maxGuests

    def __str__(self):
        return "RoomType(id={0}, description={1},maxGuests={2})".format(
            self.id, self.description, self.maxGuests
        )

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "maxGuests": self.maxGuests,
        }
