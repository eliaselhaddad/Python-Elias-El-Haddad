from math import pi
import matplotlib.pyplot as plt

class Circle:

    def __init__(self, x: float, y: float, radius: float) -> None:
        self.x = x
        self.y = y
        self.radius = radius

        if not isinstance(x, (int, float)):
            raise TypeError("x must be int or float")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be int or float")
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must int or float")

    def __repr__(self) -> str:
        return f"Circle(x = {self.x}, y = {self.y}, radius = {self.radius})"

    def __str__(self) -> str:
        pass

    @property
    def area(self) -> float:
        return pi*self.radius**2

    @property
    def circumference(self) -> float:
        return 2*pi*self.radius

    def __eq__(self, other: object) -> bool:
        if self.area == other.area:
            return True
        else:
            return False
    def __gt__(self, other) -> bool:
        if self.area > other.area:
            return True
        else:
            return False

    def __lt__(self, other) -> bool:    
        if self.area < other.area:
            return True
        else:
            return False

    def __ge__(self, other) -> bool:
        if self.area >= other.area:
            return True
        else:
            return False

    def __le__(self, other) -> bool:
        if self.area <= other.area:
            return True
        else:
            return False


class Rectangle:

    def __init__(self, x: float, y: float, width: float, height: float) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        if not isinstance(x, (int, float)):
            raise TypeError("x must be int or float")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be int or float")
        if not isinstance(width, (int, float)):
            raise TypeError("width must be int or float")
        if not isinstance(height, (int, float)):
            raise TypeError("height must be int or float")

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        return 2*(self.width + self.height)

    



