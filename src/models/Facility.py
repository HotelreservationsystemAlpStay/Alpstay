import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from controller.Validator import Validator

class Facility:
    def __init__(self, id: int, name: str) -> None:
        self.validator = Validator()
        self.validator.checkID(id)
        self.validator.checkStr(name, "name")
        self.id = id
        self.name = name

    """
    @property
    def id(self) -> int:
        return self.id

    @id.setter
    def setId(self, id: int) -> None:
        self.validator.checkID(id)
        self.id = id

    @property
    def name(self) -> str:
        return self.name

    @name.setter
    def setName(self, name: str) -> None:
        self.validator.checkStr(name, "name")
        self.name = name
    """

    def __str__(self):
        return "Facility(id={0}, name={1})".format(self.id, self.name)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }