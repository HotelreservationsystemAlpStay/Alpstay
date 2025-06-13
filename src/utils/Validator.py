# @staticmethod ermöglicht es die Methoden ohne das Objekt aufzurufen, also wenn ich z. B. bei Hotel sternen prüfen möchte
# kann ich einfach sagen Validator.checkInteger(min_stars)
from datetime import date
import re


class Validator:

    @staticmethod
    def checkInteger(value: int, name: str):
        """Check if value is an integer."""
        if not isinstance(value, int):
            raise ValueError(f"{name} must be a whole number")

    @staticmethod
    def checkPositiveInteger(value: int, name: str):
        """Check if value is a positive integer."""
        Validator.checkInteger(value, name)
        if value < 0:
            raise ValueError(f"{name} must be positive")

    @staticmethod
    def checkFloat(value: float, name: str):
        """Check if value is a float."""
        if not isinstance(value, float):
            raise ValueError(f"{name} must be a float")

    @staticmethod
    def checkPositiveFloat(value: float, name: str):
        """Check if value is a positive float."""
        Validator.checkFloat(value, name)
        if value < 0:
            raise ValueError(f"{name} must be positive")

    @staticmethod
    def checkStars(value: int):
        """Check if value is a valid star rating (1-5)."""
        Validator.checkInteger(value, "Stars")
        if value < 1 or value > 5:
            raise ValueError("Stars must be between 1 and 5")

    @staticmethod
    def checkID(value: int, name="ID"):
        """Check if value is a valid positive ID."""
        Validator.checkInteger(value, name)
        if value <= 0:
            raise ValueError(f"{name} must be a positive number")

    @staticmethod
    def checkStr(value: str, name: str):
        """Check if value is a non-empty string."""
        if not isinstance(value, str):
            raise ValueError(f"{name} has to be of type string")
        if not value.strip():
            raise ValueError(f"{name} must not be empty")

    @staticmethod
    def checkDate(value: date, name: str):
        """Check if value is a valid date object."""
        if not isinstance(value, date):
            raise ValueError(f"{name} has to be of type datetime.date")

    @staticmethod
    def checkDateDifference(valueFirstDate: date, valueSecondDate: date):
        """Check that first date is before second date."""
        if valueFirstDate >= valueSecondDate:
            raise ValueError("Your check-out date must be after your check-in date")

    @staticmethod
    def checkDateFormat(value: date, name: str):
        """Check if value has a valid date format."""
        if not isinstance(value, date):
            raise ValueError(f"{name} has to be of type date")
        if not value.strip():
            raise ValueError(f"{name} must not be empty")
        try:
            date.fromisoformat(value)
        except ValueError:
            raise ValueError(f"{name} is not a valid date format (YYYY-MM-DD)")

    @staticmethod
    def checkDates(check_in_date: date, check_out_date: date):
        """Check that check-in date is before check-out date."""
        if check_in_date >= check_out_date:
            raise ValueError("Check-in date must be before check-out date")

    @staticmethod
    def checkBoolean(value: bool, name: str):
        """Check if value is a boolean."""
        if not isinstance(value, bool):
            raise ValueError(f"{name} has to be of type boolean")

    @staticmethod
    def checkEmail(value: str, name: str = "Email"):
        """Check if value is a valid email format."""
        Validator.checkStr(value, name)
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, value):
            raise ValueError(f"Invalid {name} format")
