class Facility:
    def __init__(self, id: int, name: str) -> None:
        self._validateId(id)
        self._validateName(name)
        
        self._id = id
        self._name = name
        
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

    @property
    def getId(self) -> int:
        return self._id

    @getId.setter
    def setId(self, id: int) -> None:
        self._id = id

    @property
    def getName(self) -> str:
        return self._name
    
    @getName.setter
    def setName(self, name: str) -> None:
        self._name = name
