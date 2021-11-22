from math import pi

class Shape:

    def get_area(self):
        return self._area

    def get_perimeter(self):
        return self._perimeter

    def get_circumference(self):
        return self._circumference

class Rectangle(Shape):
    def __init__(self, height, length):
        self._height = height
        self._length = length
        self._area = length * height
        self._perimeter= (2 * length) + (2 * height)


class Square(Shape):
    def __init__(self, side_length):
        self._sides = 4
        self._side_length = side_length
        self._area = side_length**2
        self._perimeter = side_length * self._sides

class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius
        self._diameter = radius*2
        self._area = pi*self._radius**2


s = Square(5)
r = Rectangle(5, 10)

print(s.get_perimeter())
print(s.get_area())

print(r.get_perimeter())
print(r.get_area())