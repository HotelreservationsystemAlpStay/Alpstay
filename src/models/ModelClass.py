class ModelClass:
    def __init__(self):
        self.firstname = "lorem"
        self.lastname = "ipsum"
        self.age = 31
        self.salary = 4560.35

    def toNewQuery(self):
        returnList = [[],[]]
        returnList[0].append("firstname")
        returnList[1].append(self.firstname)
        return returnList