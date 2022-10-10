from math import pi
import matplotlib.pyplot as plt


class Shapes:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

        if not isinstance(x, (int, float)):
            raise TypeError("x must be int or float")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be int or float")

    def __str__(self):
        return f"Shape with x: {self.x} and y: {self.y}"

    def __repr__(self):
        return f"Shape({self.x}, {self.y})"

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

    def translate(self, x, y) -> None:
        if not isinstance(x, (int, float)):
            raise TypeError("x must be int or float")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be int or float")
        self.x += x
        self.y += y


class Circle(Shapes):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

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

    def is_inside(self, x, y) -> bool:
        distance = ((self.x - x) ** 2 + (self.y - y) ** 2)
        if distance <= self.radius:
            return True
        else:
            return False

    def is_circle_unit(self) -> bool:
        if self.radius == 1:
            return True
        else:
            return False


class Rectangle(Shapes):

    def __init__(self, x, y, width, height) -> None:
        super().__init__(x, y)
        self.width = width
        self.height = height

        if not isinstance(width, (int, float)):
            raise TypeError("Width must int or float")
        if not isinstance(height, (int, float)):
            raise TypeError("Height must int or float")

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        return 2*(self.width + self.height)

    def __eq__(self, other: object) -> bool:
        if self.area == other.area:
            return True
        else:
            return False

    def is_inside(self, x, y) -> bool:
        distance = ((self.x - x) ** 2 + (self.y - y) ** 2)
        if distance <= self.width:
            return True
        else:
            return False

    def is_square(self) -> bool:
        if self.width == self.height:
            return True
        else:
            return False

    



