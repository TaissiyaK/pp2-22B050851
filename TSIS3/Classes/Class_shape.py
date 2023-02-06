class Shape:
    def __init__(self,length):
        self.length = length
class Square(Shape):
    def area(self):
        return 0
    
    
figure = Square(int(input()))
print(Square.area(figure))