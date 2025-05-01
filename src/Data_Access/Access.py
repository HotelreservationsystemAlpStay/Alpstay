from Base_Access_Controller import Base_Access_Controller
from src.models import ModelClass

class Access:
    def __init__(self, dbcontroller: Base_Access_Controller, type: str) -> None:
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