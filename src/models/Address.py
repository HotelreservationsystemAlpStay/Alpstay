class Address:
    def __init__(self, id: int, street: str, city: str, zip: str):
        self.id = id
        self.street = street
        self.city = city
        self.zip = zip

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
