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
        self.self.validator.checkStr(description, "description")
        self.description = description

    @property
    def getMaxGuests(self) -> int:
        return self.maxGuests

    @getMaxGuests.setter
    def setMaxGuests(self, maxGuests: int) -> None:
        self.validator.checkPositiveInteger(maxGuests, "maxGuest")
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
