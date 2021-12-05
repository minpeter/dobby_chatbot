class User:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def getName(self):
        return self.name
    
    def getNumber(self):
        return self.number
    
    def dropNumber(self):
        self.number -= 1