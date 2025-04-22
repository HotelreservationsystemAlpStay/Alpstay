class Address:
    def __init__(self, id: int, street: str, city: str, zip: str) -> None:
        self._validateId(id)
        self._validateStreet(street)
        self._validateCity(city)
        self._validateZip(zip)

        self.id = id
        self.street = street
        self.city = city
        self.zip = zip

    def _validateId(self, id: int) -> None:
        if not isinstance(id, int):
            raise TypeError("ID must be an integer")
        if id <= 0:
            raise ValueError("ID must be positive")

    def _validateStreet(self, street: str) -> None:
        if not isinstance(street, str):
            raise TypeError("Strasse must be a String")
        if not street.strip():
            raise ValueError("Strasse must not be empty")

    def _validateCity(self, city: str) -> None:
        if not isinstance(city, str):
            raise TypeError("Stadt must be a String")
        if not city.strip():
            raise ValueError("Stadt must not be empty")

    def _validateZip(self, zip: str) -> None:
        if not isinstance(zip, str):
            raise TypeError("Postleihzahl must be a String")
        if not zip.strip():
            raise ValueError("Postleihzahl must not be empty")

    @property
    def getId(self) -> int:
        return self.id

    @getId.setter
    def setId(self, id: int) -> None:
        self._validateId(id)
        self.id = id

    @property
    def getStreet(self) -> str:
        return self.street

    @getStreet.setter
    def setStreet(self, street: str) -> None:
        self._validateStreet(street)
        self.street = street

    @property
    def getCity(self) -> str:
        return self.city

    @getCity.setter
    def setCity(self, city: str) -> None:
        self._validateCity(city)
        self.city = city

    @property
    def getZip(self) -> str:
        return self.zip

    @getZip.setter
    def setZip(self, zip: str) -> None:
        self._validateZip(zip)
        self.zip = zip

    def __str__(self) -> str:
        return "Address(id={0},street={1},zip={2},city={3})".format(
            self.id, self.street, self.zip, self.city
        )

    def to_dict(self):
        return {
            "id": self.id,
            "street": self.street,
            "zip": self.zip,
            "city": self.city,
        }
