class Address():
    def __init__(self, id: int, street: str, city: str, zip: str) -> None:
        self.__id = id
        self.__street = street
        self.__city = city
        self.__zip = zip

    def getId(self) -> int:
        return self.__id

    def setId(self, id: int) -> None:
        self.__id = id

    def getStreet(self) -> str:
        return self.__street

    def setStreet(self, street: int) -> None:
        self.__street = street

    def getCity(self) -> str:
        return self.__city

    def setCity(self, city: str) -> None:
        self.__city = city

    def getZip(self) -> str:
        return self.__zip

    def setZip(self, zip: str) -> None:
        self.__zip = zip

    def __str__(self) -> str:
        """return class in type string

        Returns:
            str: formatted address
        """
        return "{0}\n{1} {2}".format(self.__street, self.__zip, self.__city)
