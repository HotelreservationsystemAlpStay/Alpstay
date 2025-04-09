class User:
    def __init__(self, id: int, username: str, password: str, role: str) -> None:
        self._validateId(id)
        self._validateUsername(username)
        self._validatePassword(password)
        self._validateRole(role)

        self.id = id
        self.username = username
        self.password = password
        self.role = role

    def _validateId(self, id: int) -> None:
        if not isinstance(id, int):
            raise TypeError("ID must be an integer")
        if id <= 0:
            raise ValueError("ID must be positive")

    def _validateUsername(self, username: str) -> None:
        if not isinstance(username, str):
            raise TypeError("Username must be a String")
        if not username.strip():
            raise ValueError("Username must not be empty")

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


""" 
    @property
    def getId(self) -> int:
        return self.id

    @getId.setter
    def setId(self, id: int) -> None:
        self.id = id

    @property
    def getUsername(self) -> str:
        return self.username

    @getUsername.setter
    def setDescription(self, username: str) -> None:
        self.username = username
    
    @property
    def getPassword(self) -> str:
        return self.password

    @getPassword.setter
    def setDescription(self, password: str) -> None:
        self.password = password
    
    @property
    def getRole(self) -> str:
        return self.role

    @getRole.setter
    def setDescription(self, role: str) -> None:
        self.role = role
        """
