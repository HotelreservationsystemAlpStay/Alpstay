class Validator:
    def __init__(self):
        pass

        
    def checkInteger(value: int, name: str):
        if not isinstance(value, int):
            raise TypeError("{0} must be an integer".format(name))
        
    def checkID(self, value: int):
        self.checkID(value, "Id")
        if value <= 0:
            raise ValueError("{0} must be positive".format("Id"))