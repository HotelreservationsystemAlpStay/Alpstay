class RoomType():
    def __init__(self, id: int, description: str, maxGuests: int) -> None:
        self.__id = id
        self.__description = description
        self.__maxGuests = maxGuests

    def getId(self) -> int:
        return self.__id

    def setId(self, id: int) -> None:
        self.__id = id

    def getDescription(self) -> str:
        return self.__description

    def setDescription(self, description: str) -> None:
        self.__description = description

    def getMaxGuests(self) -> str:
        return self.__maxGuests

    def setMaxGuests(self, maxGuests: int) -> None:
        self.__maxGuests = maxGuests
