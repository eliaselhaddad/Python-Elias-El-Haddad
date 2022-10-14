from math import pi


class Shapes:
    '''Shapes class is a parent class to Circle and Rectangle classes'''
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    @property
    def x(self) -> float:
        return self._x
    
    @x.setter
    def x(self, x: float) -> None:
        if not isinstance(x, (int, float)):
            raise TypeError("x must be int or float")
        self._x = x
        
    @property
    def y(self) -> float:
        return self._y
    
    @y.setter
    def y(self, y: float) -> None:
        if not isinstance(y, (int, float)):
            raise TypeError("y must be int or float")
        self._y = y

    def __str__(self) -> str:
        return f"Shape with x: {self.x} and y: {self.y}"

    def __repr__(self) -> str:
        return f"Shape({self.x}, {self.y})"

    def __gt__(self, other) -> bool:
        return self.area > other.area

    def __lt__(self, other) -> bool:    
        return self.area < other.area

    def __ge__(self, other) -> bool:
        return self.area >= other.area

    def __le__(self, other) -> bool:
        return self.area <= other.area

    def translate(self, x: float, y: float) -> None:
        '''a method that makes it possible to move x and y to a new position '''
        if not isinstance(x, (float, int)):
            raise TypeError("x must be int or float")
        if not isinstance(y, (float, int)):
            raise TypeError("y must be int or float")
        self.x += x
        self.y += y


class Circle(Shapes):
    '''a child class to Shapes class'''
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, radius: float) -> None:
        if not isinstance(radius, (int, float)):
            raise TypeError("raius must be int or float")
        self._radius = radius

    def __repr__(self) -> str:
        return f"Circle(x = {self.x}, y = {self.y}, radius = {self.radius})"

    def __str__(self) -> str:
        return f"x = {self.x}, y = {self.y}, radius = {self.radius}"

    @property
    def area(self) -> float:
        '''read-only property to calculate the area of a circle'''
        return pi*self.radius**2

    @property
    def circumference(self) -> float:
        '''read-only property to calculate the circumference of a circle'''
        return 2*pi*self.radius

    def __eq__(self, other: object) -> bool:
        return self.area == other.area

    def is_inside(self, x, y) -> bool:
        '''a method to check if a point is inside the circle'''
        if not isinstance(x, (float, int)):
            raise TypeError("x must be int or float")
        if not isinstance(y, (float, int)):
            raise TypeError("y must be int or float")
        distance = ((self.x - x) ** 2 + (self.y - y) ** 2)
        return distance < self.radius
        

    def is_circle_unit(self) -> bool:
        '''a method to check if a circle is a unit circle'''
        return self.radius == 1


class Rectangle(Shapes):
    '''a child class to Shapes class'''
    def __init__(self, x, y, width, height) -> None:
        super().__init__(x, y)
        self.width = width
        self.height = height

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, width) -> None:
        if not isinstance(width, (int, float)):
            raise TypeError("width must be int or float")
        if width <= 0:
            raise ValueError("width must be positive")
        self._width = width

    @property
    def height(self) -> float:
        return self._height
    
    @height.setter
    def height(self, height: float) -> None:
        if not isinstance(height, (int, float)):
            raise TypeError("height must be int or float")
        if height <= 0:
            raise ValueError("height must be positive")
        self._height = height

    def __repr__(self) -> str:
        return f"Rectangle(x = {self.x}, y = {self.y}, width = {self.width}, height = {self.height})"

    def __str__(self) -> str:
        return f"x = {self.x}, y = {self.y}, width = {self.width}, height = {self.height}"

    @property
    def area(self) -> float:
        '''read-only property to calculate the area of a rectangle'''
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        '''read-only property to calculate the perimeter of a rectangle'''
        return 2*(self.width + self.height)

    def __eq__(self, other: object) -> bool:
        return self.area == other.area

    def is_inside(self, x, y) -> bool:
        if not isinstance(x, (float, int)):
            raise TypeError("x must be int or float")
        if not isinstance(y, (float, int)):
            raise TypeError("y must be int or float")
        '''a method to check if a point is inside a rectangle'''
        return (self.x - self.width / 2 <= x <= self.x + self.width / 2) and (self.y - self.height / 2 <= y <= self.y + self.height / 2)

    def is_square(self) -> bool:
        '''a method to check if rectangle is a square'''
        return self.width == self.height
        

    



