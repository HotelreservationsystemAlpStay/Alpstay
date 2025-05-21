class Facility:
    def __init__(self, id: int, name: str) -> None:
        self._id = id
        self._name = name

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        self._id = id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    def __str__(self):
        return "Facility(id={0}, name={1})".format(self._id, self._name)
    
    def to_dict(self):
        return {
            'id': self._id,
            'name': self._name
        }