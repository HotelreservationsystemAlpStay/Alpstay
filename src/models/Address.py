class Address:
    def __init__(self, id: int, street: str, city: str, zip: str):
        """Initialize an Address with id, street, city, and zip code."""
        self._id = id
        self._street = street
        self._city = city
        self._zip = zip

    @property
    def id(self) -> int:
        """Get the address ID."""
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        """Set the address ID."""
        self._id = id

    @property
    def street(self) -> str:
        """Get the street address."""
        return self._street

    @street.setter
    def street(self, street: str) -> None:
        """Set the street address."""
        self._street = street

    @property
    def city(self) -> str:
        """Get the city name."""
        return self._city

    @city.setter
    def city(self, city: str) -> None:
        """Set the city name."""
        self._city = city

    @property
    def zip(self) -> str:
        """Get the zip code."""
        return self._zip

    @zip.setter
    def zip(self, zip_code: str) -> None: # Renamed parameter to avoid conflict with module
        """Set the zip code."""
        self._zip = zip_code

    def __str__(self) -> str:
        """Return string representation of the address."""
        return "Address(id={0},street={1},zip={2},city={3})".format(
            self._id, self._street, self._zip, self._city
        )

    def to_dict(self):
        """Convert address to dictionary format."""
        return {
            "id": self._id,
            "street": self._street,
            "zip": self._zip,
            "city": self._city,
        }
