# This is a throwaway file for remedial oop training

#^ From Think Python chapters 16-18
from math import sqrt

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    """Takes in width, height and a Point object"""

    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = (corner.x, corner.y)

point_1 = Point(1, 2)
rectangle_1 = Rectangle(4, 5, point_1)

print(rectangle_1.corner)

