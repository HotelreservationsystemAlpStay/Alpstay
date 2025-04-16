class Guest:

    
#def init statement
    def __init__(self, guest_id: int, name: str, surname: str, phone_nr: int, email: str, zip: int, address: str) -> None:
        self._validateId(guest_id)
        self._validateName(name)
        self._validateSurname(surname)
        self._validatePhoneNr(phone_nr)
        self._validateEmail(email)
        self._validateZip(zip)
        self._validateAddress(address)

        self._guest_id = guest_id
        self._name = name
        self._surname = surname
        self._phone_nr = phone_nr
        self._email = email
        self._zip = zip
        self._address = address


    
#def validate statements    
    def _validateId(self, guest_id: int) -> None:
        if not isinstance(guest_id, int):
            raise ValueError("Guest-ID muss eine ganze Zahl sein")

    def _validateName(self, name: str) -> None:
        if not isinstance(name, str):
            raise ValueError("Der Name muss ein String sein")

    def _validateSurname(self, surname: str) -> None:
        if not isinstance(surname, str):
            raise ValueError("Nachname muss ein String sein")

    def _validatePhoneNr(self, phone_nr: int) -> None:
        if not isinstance(phone_nr, int):
            raise ValueError("Die Telefonnummer muss eine ganze Zahl sein")

    def _validateEmail(self, email: str) -> None:
        if not isinstance(email, str):
            raise ValueError("Die Email muss ein String sein")

    def _validateZip(self, zip: int) -> None:
        if not isinstance(zip, int):
            raise ValueError("Postleitzahl muss eine Zahl sein")

    def _validateAddress(self, address: str) -> None:
        if not isinstance(address, str):
            raise ValueError("Die Adresse muss ein String sein")



#if needed leave property (getter and setter)
"""
    @property
    def guest_id(self) -> int:
        return self._guest_id

    @guest_id.setter
    def guest_id(self, guest_id: int) -> None:
        self._guest_id = guest_id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def surname(self) -> str:
        return self._surname

    @surname.setter
    def surname(self, surname: str) -> None:
        self._surname = surname

    @property
    def phone_nr(self) -> int:
        return self._phone_nr

    @phone_nr.setter
    def phone_nr(self, phone_nr: int) -> None:
        self._phone_nr = phone_nr

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str) -> None:
        self._email = email

    @property
    def zip(self) -> int:
        return self._zip

    @zip.setter
    def zip(self, zip: int) -> None:
        self._zip = zip

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, address: str) -> None:
        self._address = address

"""
