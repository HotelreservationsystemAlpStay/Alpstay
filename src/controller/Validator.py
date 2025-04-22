class Validator:
    def __init__(self):
        pass
        
    def checkInteger(value: int, name: str, errormessage="") -> None:
        if not isinstance(value, int):
            if errormessage != "":
                raise TypeError(errormessage)
            raise TypeError("{0} must be an integer".format(name))
        
    def checkID(self, value: int):
        self.checkInteger(value, "Id")
        if value <= 0:
            raise ValueError("{0} must be positive".format("Id"))