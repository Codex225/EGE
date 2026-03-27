import math

class Square:
    def __init__(self, side):
        self.side = side

    def extrude(self, h):
        return self.side ** 2 * h


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def extrude(self, h):
        return self.a * h * self.b

class Triangle:
    def __init__(self, side):
        self.side = side

    def extrude(self, h):
        return self.side ** 2 * 3 ** 0.5 * h / 4

sq = Square(1)
rec = Rectangle(1, 2)
tr = Triangle(1)
#cir = Circle(1)
for item in (sq, rec, tr): #cir):
    print(item.extrude(1))