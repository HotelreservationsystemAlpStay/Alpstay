#@staticmethod ermöglicht es die Methoden ohne das Objekt aufzurufen, also wenn ich z. B. bei Hotel sternen prüfen möchte
#kann ich einfach sagen Validator.checkInteger(min_stars)
from datetime import date

class Validator:

    @staticmethod
    def checkInteger(value: int, name: str):
        if not isinstance(value, int):
                raise ValueError(f"{name} must be a whole number")
    
    @staticmethod
    def checkPositiveInteger(value: int, name: str):
        Validator.checkInteger(value, name)
        if value < 0:
             raise ValueError(f"{name} must be positive")

    @staticmethod
    def checkFloat(value: float, name: str):
        if not isinstance(value, float):
            raise ValueError(f"{name} must be a float")
    
    @staticmethod
    def checkPositiveFloat(value: float, name: str):
        Validator.checkFloat(value, name)
        if value < 0:
            raise ValueError(f"{name} must be positive")

    @staticmethod
    def checkStars(value:int):
         Validator.checkInteger(value, "Stars")
         if value < 1 or value > 5:
              raise ValueError("Stars must be between 1 and 5")
        
    @staticmethod    
    def checkID(value: int):
        Validator.checkInteger(value, "ID")
        if value <= 0:
            raise ValueError("ID must be a positive number")
        
    @staticmethod
    def checkStr(value: str, name:str):
        if not isinstance(value, str):
            raise ValueError(f"{name} has to be of type string")
        if not value.strip():
            raise ValueError(f"{name} must not be empty")
        
    @staticmethod
    def checkDate(value: date, name: str):
        if not isinstance(value, date):
            raise ValueError(f"{name} has to be of type datetime.date")
    
    @staticmethod
    def checkDateDifference(valueFirstDate: date, valueSecondDate:date):
        Validator.checkDate(valueFirstDate)
        Validator.checkDate(valueSecondDate)
        if valueSecondDate > valueFirstDate:
            raise ValueError("Last Date is before first Date")