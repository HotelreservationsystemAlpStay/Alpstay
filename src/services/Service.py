from src.controller import DataBaseController
from src.models import ModelClass

class Service:
    def __init__(self, dbcontroller: DataBaseController, type: str) -> None:
        self._controller = dbcontroller
        self._type = type

    def fetchAll(self) -> list:
        query = "SELECT * FROM {0}".format(self._type)
        return self._controller.fetchall(query)
    
    def createNew(self, instance:ModelClass):
        pass

    def updateOne(self):
        pass

    def updateAll(self):
        pass

    def deleteOne(self):
        pass