class Address:
    def __init__(self, id: int, street: str, city: str, zip: str) -> None:
        self._validateId(id)
        self._validateStreet(street)
        self._validateCity(city)
        self._validateZip(zip)
        
        self._id = id
        self._street = street
        self._city = city
        self._zip = zip

    def _validateId(self, id: int) -> None:
        if not isinstance(id, int):
            raise TypeError("ID muss eine Ganzzahl sein")
        if id <= 0:
            raise ValueError("ID muss positiv sein")

    def _validateStreet(self, street: str) -> None:
        if not isinstance(street, str):
            raise TypeError("Strasse muss ein String sein")
        if not street.strip():
            raise ValueError("Strasse darf nicht leer sein")
        
    def _validateCity(self, city: str) -> None:
        if not isinstance(city, str):
            raise TypeError("Stadt muss ein String sein")
        if not city.strip():
            raise ValueError("Stadt darf nicht leer sein")
        
    def _validateZip(self, zip: str) -> None:
        if not isinstance(zip, str):
            raise TypeError("Postleihzahl muss ein String sein")
        if not zip.strip():
            raise ValueError("Postleihzahl darf nicht leer sein")

    @property    
    def getId(self) -> int:
        return self._id

    @getId.setter
    def setId(self, id: int) -> None:
        self._id = id

    @property 
    def getStreet(self) -> str:
        return self._street

    @getStreet.setter
    def setStreet(self, street: int) -> None:
        self._street = street

    @property 
    def getCity(self) -> str:
        return self._city

    @getCity.setter
    def setCity(self, city: str) -> None:
        self._city = city

    @property 
    def getZip(self) -> str:
        return self._zip

    @getZip.setter
    def setZip(self, zip: str) -> None:
        self._zip = zip

    def __str__(self) -> str:
        """return class in type string

        Returns:
            str: formatted address
        """
        return "{0}\n{1} {2}".format(self._street, self._zip, self._city)
