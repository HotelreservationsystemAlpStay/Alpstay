#@staticmethod ermöglicht es die Methoden ohne das Objekt aufzurufen, also wenn ich z. B. bei Hotel sternen prüfen möchte
#kann ich einfach sagen Validator.checkInteger(min_stars)
class Validator:

    @staticmethod
    def checkInteger(value: int, name: str):
        if not isinstance(value, int):
                raise ValueError(f"{name} must be a whole number")
    
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
    def checkStr(value: str):
        if not isinstance(value, str):
            raise ValueError(f"{value} has to be of type string")
        if not value.strip():
            raise ValueError(f"{value} must not be empty")