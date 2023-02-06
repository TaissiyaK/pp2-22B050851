class string:
    def __init__(self, string):
        self.string = string

    def getString(self):
        return self.string
    
    def printString(self):
        self.string = self.string.upper()
        return self.string
    
    
s = string(input())
s1 = s.getString()
s2 = s.printString()
print(s1, s2)