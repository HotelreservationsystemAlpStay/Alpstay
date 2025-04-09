from controller import DBController


class Service:
    def __init__(self, dbcontroller: DBController) -> None:
        self._controller = dbcontroller
