class Shape:
    def __init__(self, length, width):
            self.length = length
            self.width = width
class Rectangle(Shape):
    def area(self):
        return self.length*self.width
    
    
figure = Rectangle(int(input()), int(input()))
print(Rectangle.area(figure))