class Facility:
    def __init__(self, id: int, name: str) -> None:
        self._validateId(id)
        self._validateName(name)

        self.id = id
        self.name = name

    def _validateId(self, id: int) -> None:
        if not isinstance(id, int):
            raise TypeError("ID must be an integer")
        if id <= 0:
            raise ValueError("ID must be positive")

    def _validateName(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Name must be a String")
        if not name.strip():
            raise ValueError("Name must not be empty")


    @property
    def id(self) -> int:
        return self.id

    @id.setter
    def setId(self, id: int) -> None:
        self._validateId(id)
        self.id = id

    @property
    def name(self) -> str:
        return self.name

    @name.setter
    def setName(self, name: str) -> None:
        self._validateName(name)
        self.name = name

    def __str__(self):
        return "Facility(id={0}, name={2})".format(self.id, self.name)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }