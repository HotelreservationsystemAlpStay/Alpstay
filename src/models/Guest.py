import datetime

class Guest:
    def __init__(self, guest_id: int, first_name: str, last_name: str, email: str, address_id: int, age: int, birthdate: datetime.date, country: str) -> None:
        """Initialize a Guest with all personal details."""
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
        """Get the guest ID."""
        return self._guest_id

    @guest_id.setter
    def guest_id(self, guest_id: int) -> None:
        """Set the guest ID."""
        self._guest_id = guest_id

    @property
    def first_name(self) -> str:
        """Get the first name."""
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str) -> None:
        """Set the first name."""
        self._first_name = first_name

    @property
    def last_name(self) -> str:
        """Get the last name."""
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str) -> None:
        """Set the last name."""
        self._last_name = last_name

    @property
    def email(self) -> str:
        """Get the email address."""
        return self._email

    @email.setter
    def email(self, email: str) -> None:
        """Set the email address."""
        self._email = email

    @property
    def address_id(self) -> int:
        """Get the address ID."""
        return self._address_id

    @address_id.setter
    def address_id(self, address_id: int) -> None:
        """Set the address ID."""
        self._address_id = address_id

    @property
    def age(self) -> int:
        """Get the age."""
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        """Set the age."""
        self._age = age

    @property
    def birthdate(self) -> datetime.date:
        """Get the birthdate."""
        return self._birthdate

    @birthdate.setter
    def birthdate(self, birthdate: datetime.date) -> None:
        """Set the birthdate."""
        self._birthdate = birthdate

    @property
    def country(self) -> str:
        """Get the country."""
        return self._country

    @country.setter
    def country(self, country: str) -> None:
        """Set the country."""
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
