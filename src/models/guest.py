class Guest:
  def _init_ (self, guest_id: int, name: str, surname: str, phone_nr: int, email: str, zip: int, address: str)
    if not isinstance(guest_id, int):
            raise ValueError("Die Guest-ID muss eine Integer sein")
    if not isinstance(name, str):
            raise ValueError("Der Name muss eine String sein")
    if not isinstance(surname, str):
            raise ValueError("Der Surname muss eine String sein")
    if not isinstance(phone_nr, int):
            raise ValueError("Die Phone_nr muss eine Integer sein")
    if not isinstance(email, str):
            raise ValueError("Die Email muss eine String sein")
    if not isinstance(zip, int):
            raise ValueError("Die ZIP muss eine Integer sein")
    if not isinstance(address, str):
            raise ValueError("Die Address muss eine String sein")
    self._id = guest_id
    self._name = name
    self._surname = surname
    self._phone_nr = phone_nr
    self._email = email
    self._zip = zip
    self._address = address

