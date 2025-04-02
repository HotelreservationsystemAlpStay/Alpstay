class Facility():
    def __init__(self, id: int, name: str) -> None:
        self.__id = id
        self.__name = name

    def setId(self, id: int) -> None:
        self.__id = id

    def getId(self) -> int:
        return self.__id

    def setName(self, name: str) -> None:
        self.__name = name

    def getName(self) -> str:
        return self.__name
