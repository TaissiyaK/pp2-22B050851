class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)
    def move(self, x1, y1):
        self.x = x1
        self.y = y1
        return Point(self.x , self.y)
    def dist(self):
        return (( self.x**2 + self.y**2 ) ** 0.5)


point = Point(int(input()),int(input()))
Point.show(point)

distance = Point.dist(point)
print(distance)

point = Point.move(point,int(input()),int(input()))
Point.show(point)

