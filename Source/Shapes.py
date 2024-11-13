import math

class shape:

    def shape_area(self):
        pass
    def shape_perimeter(self):
        pass

class circle(shape):

    def __init__(self,radius,diameter):
        self.radius = radius
        self.diameter = diameter
    def area(self):
        return math.pi * self.radius **2

    def perimeter(self):
        return 2 * math.pi * self.radius

class rectangle(shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def __eq__(self, other):
        if not isinstance(other,rectangle):
            return False
        return self.length ==  other.length and self.breadth == other.breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2* (self.length + self.breadth)