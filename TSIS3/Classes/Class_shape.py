class Shape:
    def __init__(self):
        self.area = 0
    def area(self):
        return self.area
class Square(Shape):
    def __init__(self,length):
        self.length = length
    def area(self):
        return self.length*self.length
    
    
figure = Square(int(input()))
print(Square.area(figure))