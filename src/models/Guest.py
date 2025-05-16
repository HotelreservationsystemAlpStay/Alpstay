import datetime
from src.utils.Validator import Validator

class Guest:

    def __init__(self, guest_id: int, first_name: str, last_name: str, email: str, address_id: int, age: int, birthdate: datetime.date, country: str) -> None:
        Validator.checkID(guest_id, "Guest-ID")
        Validator.checkStr(first_name, "First name")
        Validator.checkStr(last_name, "Last name")
        Validator.checkEmail(email, "Email")
        Validator.checkID(address_id, "Address ID")
        Validator.checkPositiveInteger(age, "Age")
        Validator.checkDate(birthdate, "Birthdate")
        Validator.checkStr(country, "Country")

        self._guest_id = guest_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._address_id = address_id
        self._age = age
        self._birthdate = birthdate
        self._country = country


    @property
    def guest_id(self) -> int:
        return self._guest_id

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str) -> None:
        Validator.checkStr(first_name, "First name")
        self._first_name = first_name

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str) -> None:
        Validator.checkStr(last_name, "Last name")
        self._last_name = last_name

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str) -> None:
        Validator.checkEmail(email, "Email")
        self._email = email

    @property
    def address_id(self) -> int:
        return self._address_id

    @address_id.setter
    def address_id(self, address_id: int) -> None:
        Validator.checkID(address_id, "Address ID")
        self._address_id = address_id

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        Validator.checkPositiveInteger(age, "Age")
        self._age = age

    @property
    def birthdate(self) -> datetime.date:
        return self._birthdate

    @birthdate.setter
    def birthdate(self, birthdate: datetime.date) -> None:
        Validator.checkDate(birthdate, "Birthdate")
        self._birthdate = birthdate

    @property
    def country(self) -> str:
        return self._country

    @country.setter
    def country(self, country: str) -> None:
        Validator.checkStr(country, "Country")
        self._country = country
