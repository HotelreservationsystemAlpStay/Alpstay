class ModelClass:
    def __init__(self):
        self._firstname = "lorem"
        self._lastname = "ipsum"
        self._age = 31
        self._salary = 4560.35

    @property
    def firstname(self) -> str:
        return self._firstname

    @firstname.setter
    def firstname(self, firstname: str) -> None:
        self._firstname = firstname

    @property
    def lastname(self) -> str:
        return self._lastname

    @lastname.setter
    def lastname(self, lastname: str) -> None:
        self._lastname = lastname

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        self._age = age

    @property
    def salary(self) -> float:
        return self._salary

    @salary.setter
    def salary(self, salary: float) -> None:
        self._salary = salary

    # Comment one
    def toNewQuery(self):
        returnList = [[],[]]
        returnList[0].append("firstname") # Or self._firstname if the key should be dynamic
        returnList[1].append(self._firstname)
        # Assuming you want to include other attributes as well:
        # returnList[0].extend(["lastname", "age", "salary"])
        # returnList[1].extend([self._lastname, self._age, self._salary])
        return returnList