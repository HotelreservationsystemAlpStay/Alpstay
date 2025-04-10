from src.controller import DataBaseController


class Service:
    def __init__(self, dbcontroller: DataBaseController) -> None:
        self._controller = dbcontroller
