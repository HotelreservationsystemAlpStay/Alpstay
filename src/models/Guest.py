import datetime

class Guest:
    def __init__(self, guest_id: int, first_name: str, last_name: str, email: str, address_id: int, age: int, birthdate: datetime.date, country: str) -> None:
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

    @guest_id.setter
    def guest_id(self, guest_id: int) -> None:
        self._guest_id = guest_id

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str) -> None:
        self._first_name = first_name

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str) -> None:
        self._last_name = last_name

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str) -> None:
        self._email = email

    @property
    def address_id(self) -> int:
        return self._address_id

    @address_id.setter
    def address_id(self, address_id: int) -> None:
        self._address_id = address_id

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        self._age = age

    @property
    def birthdate(self) -> datetime.date:
        return self._birthdate

    @birthdate.setter
    def birthdate(self, birthdate: datetime.date) -> None:
        self._birthdate = birthdate

    @property
    def country(self) -> str:
        return self._country

    @country.setter
    def country(self, country: str) -> None:
        self._country = country

    def __str__(self) -> str:
        return (f"Guest(id={self._guest_id}, name={self._first_name} {self._last_name}, "
                f"email={self._email}, country={self._country})")

    def to_dict(self) -> dict:
        return {
            'guest_id': self._guest_id,
            'first_name': self._first_name,
            'last_name': self._last_name,
            'email': self._email,
            'address_id': self._address_id,
            'age': self._age,
            'birthdate': self._birthdate.isoformat() if self._birthdate else None,
            'country': self._country
        }
