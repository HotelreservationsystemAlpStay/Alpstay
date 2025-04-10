class Facility:
    def __init__(self, id: int, name: str) -> None:
        self._validateId(id)
        self._validateName(name)

        self.id = id
        self.name = name

    def _validateId(self, id: int) -> None:
        if not isinstance(id, int):
            raise TypeError("ID muss eine Ganzzahl sein")
        if id <= 0:
            raise ValueError("ID muss positiv sein")

    def _validateName(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Name muss ein String sein")
        if not name.strip():
            raise ValueError("Name darf nicht leer sein")


"""
    @property
    def id(self) -> int:
        return self.id

    @id.setter
    def setId(self, id: int) -> None:
        self.id = id

    @property
    def name(self) -> str:
        return self.name

    @name.setter
    def setName(self, name: str) -> None:
        self.name = name
"""
