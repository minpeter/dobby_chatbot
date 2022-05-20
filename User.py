class User:
    def __init__(self, name, number, score = 0):
        self.name = name
        self.number = number
        self.score = score

    def getName(self):
        return self.name
    
    def getNumber(self):
        return self.number
    
    def dropNumber(self):
        self.number -= 1
    
    def getScore(self):
        return self.score
    
    def addScore(self):
        self.score += 1