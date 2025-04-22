class User:
    def __init__(self, id: int, guest_id: int, password: str, role: str) -> None:
        self._validateId(id)
        self._validateGuest_id(guest_id)
        self._validatePassword(password)
        self._validateRole(role)

        self.id = id
        self.guest_id = guest_id
        self.password = password
        self.role = role

    def _validateId(self, id: int) -> None:
        if not isinstance(id, int):
            raise TypeError("ID must be an integer")
        if id <= 0:
            raise ValueError("ID must be positive")

    def _validateGuest_id(self, guest_id: int) -> None:
        if not isinstance(guest_id, int):
            raise TypeError("ID must be an integer")
        if guest_id <= 0:
            raise ValueError("ID must be positive")

    def _validatePassword(self, password: str) -> None:
        if not isinstance(password, str):
            raise TypeError("Password must be a String")
        if not password.strip():
            raise ValueError("Password must not be empty")

    def _validateRole(self, role: str) -> None:
        if not isinstance(role, str):
            raise TypeError("Role must be a String")
        if not role.strip():
            raise ValueError("Role must not be empty")

    @property
    def getId(self) -> int:
        return self.id

    @getId.setter
    def setId(self, id: int) -> None:
        self._validateId(id)
        self.id = id

    @property
    def getGuest_id(self) -> str:
        return self.guest_id

    @getGuest_id.setter
    def setDescription(self, guest_id: int) -> None:
        self._validateGuest_id(guest_id)
        self.guest_id = guest_id

    @property
    def getPassword(self) -> str:
        return self.password

    @getPassword.setter
    def setDescription(self, password: str) -> None:
        self._validatePassword(password)
        self.password = password

    @property
    def getRole(self) -> str:
        return self.role

    @getRole.setter
    def setDescription(self, role: str) -> None:
        self._validateRole(role)
        self.role = role

    def __str__(self):
        return "User(user_id={0},guest_id={1},user_role={2},user_password={3})".format(
            self.id, self.guest_id, self.role, self.password
        )

    def to_dict(self)->dict:
        return {
            'user_id': self.id,
            'guest_id': self.guest_id,
            'user_role': self.role,
            'user_password': self.password
        }