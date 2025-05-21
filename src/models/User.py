class User:
    def __init__(self, id: int, guest_id: int, password: str, role: str) -> None:
        self._id = id
        self._guest_id = guest_id
        self._password = password
        self._role = role

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        self._id = id

    @property
    def guest_id(self) -> int:
        return self._guest_id

    @guest_id.setter
    def guest_id(self, guest_id: int) -> None:
        self._guest_id = guest_id

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, password: str) -> None:
        self._password = password

    @property
    def role(self) -> str:
        return self._role

    @role.setter
    def role(self, role: str) -> None:
        self._role = role

    def __str__(self):
        return "User(user_id={0},guest_id={1},user_role={2},user_password={3})".format(
            self._id, self._guest_id, self._role, self._password
        )

    def to_dict(self)->dict:
        return {
            'user_id': self._id,
            'guest_id': self._guest_id,
            'user_role': self._role,
            'user_password': self._password
        }