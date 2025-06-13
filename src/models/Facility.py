class Facility:
    def __init__(self, id: int, name: str) -> None:
        """Initialize a Facility with id and name."""
        self._id = id
        self._name = name

    @property
    def id(self) -> int:
        """Get the facility ID."""
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        """Set the facility ID."""
        self._id = id

    @property
    def name(self) -> str:
        """Get the facility name."""
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """Set the facility name."""
        self._name = name

    def __str__(self):
        """Return string representation of the facility."""
        return "Facility(id={0}, name={1})".format(self._id, self._name)
    
    def to_dict(self):
        """Convert facility to dictionary format."""
        return {
            'id': self._id,
            'name': self._name
        }