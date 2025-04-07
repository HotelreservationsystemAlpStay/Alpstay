class User:
    def __init__(self, id:int, username: str, password: str, role: str)-> None: 
        self._validateId(id)
        self._validateUsername(username)
        self._validatePassword(password)
        self._validateRole(role)
        
        self._id = id
        self._username = username
        self._password = password
        self._role = role
    
    def _validateId(self, id: int) -> None:
        if not isinstance(id, int):
            raise TypeError("ID muss eine Ganzzahl sein")
        if id <= 0:
            raise ValueError("ID muss positiv sein")

    def _validateUsername(self, username: str) -> None:
        if not isinstance(username, str):
            raise TypeError("Benutzername muss ein String sein")
        if not username.strip():
            raise ValueError("Benutzername darf nicht leer sein")
    
    def _validatePassword(self, password: str) -> None:
        if not isinstance(password, str):
            raise TypeError("Password muss ein String sein")
        if not password.strip():
            raise ValueError("Password darf nicht leer sein")
        
    def _validateRole(self, role: str) -> None:
        if not isinstance(role, str):
            raise TypeError("Rolle muss ein String sein")
        if not role.strip():
            raise ValueError("Rolle darf nicht leer sein")
        
    @property
    def getId(self) -> int:
        return self._id

    @getId.setter
    def setId(self, id: int) -> None:
        self._id = id

    @property
    def getUsername(self) -> str:
        return self._username

    @getUsername.setter
    def setDescription(self, username: str) -> None:
        self._username = username
    
    @property
    def getPassword(self) -> str:
        return self._password

    @getPassword.setter
    def setDescription(self, password: str) -> None:
        self._password = password
    
    @property
    def getRole(self) -> str:
        return self._role

    @getRole.setter
    def setDescription(self, role: str) -> None:
        self._role = role
        