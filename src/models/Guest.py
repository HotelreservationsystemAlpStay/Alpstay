import datetime

class Guest:

    
#def init statement
    def __init__(self, guest_id: int, first_name: str, last_name: str, email: str, address_id: int, age: int, birthdate: datetime.date, country: str) -> None:
        self._validate_guest_id(guest_id)
        self._validate_first_name(first_name)
        self._validate_last_name(last_name)
        self._validate_email(email)
        self._validate_address_id(address_id)
        self._validate_age(age)
        self._validate_birthdate(birthdate)
        self._validate_country(country)

        self._guest_id = guest_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._address_id = address_id
        self._age = age
        self._birthdate = birthdate
        self._country = country


    
#def validate statements    
    def _validate_guest_id(self, guest_id: int) -> None:
        if not isinstance(guest_id, int):
            raise ValueError("Guest-ID needs to be an integer")

    def _validate_first_name(self, first_name: str) -> None:
        if not isinstance(first_name, str):
            raise ValueError("First name needs to be a string")

    def _validate_last_name(self, last_name: str) -> None:
        if not isinstance(last_name, str):
            raise ValueError("Last name needs to be a string")

    def _validate_email(self, email: str) -> None:
        if not isinstance(email, str):
            raise ValueError("Email needs to be a string")
        if "@" not in email or "." not in email.split('@')[-1]:
            raise ValueError("Invalid email format")

    def _validate_address_id(self, address_id: int) -> None:
        if not isinstance(address_id, int):
            raise ValueError("Address ID needs to be an integer")

    def _validate_age(self, age: int) -> None:
        if not isinstance(age, int):
            raise ValueError("Age needs to be an integer")
        if age < 0:
            raise ValueError("Age cannot be negative")

    def _validate_birthdate(self, birthdate: datetime.date) -> None:
        if not isinstance(birthdate, datetime.date):
            raise ValueError("Birthdate needs to be a valid date object")

    def _validate_country(self, country: str) -> None:
        if not isinstance(country, str):
            raise ValueError("Country needs to be a string")


#if needed leave property (getter and setter)
    @property
    def guest_id(self) -> int:
        return self._guest_id

    @guest_id.setter
    def guest_id(self, guest_id: int) -> None:
        self._validate_guest_id(guest_id)
        self._guest_id = guest_id

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str) -> None:
        self._validate_first_name(first_name)
        self._first_name = first_name

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str) -> None:
        self._validate_last_name(last_name)
        self._last_name = last_name

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str) -> None:
        self._validate_email(email)
        self._email = email

    @property
    def address_id(self) -> int:
        return self._address_id

    @address_id.setter
    def address_id(self, address_id: int) -> None:
        self._validate_address_id(address_id)
        self._address_id = address_id

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        self._validate_age(age)
        self._age = age

    @property
    def birthdate(self) -> datetime.date:
        return self._birthdate

    @birthdate.setter
    def birthdate(self, birthdate: datetime.date) -> None:
        self._validate_birthdate(birthdate)
        self._birthdate = birthdate

    @property
    def country(self) -> str:
        return self._country

    @country.setter
    def country(self, country: str) -> None:
        self._validate_country(country)
        self._country = country
