# from __future__ import ann
from math import pi

class Circle:

    def __init__(self, x: float, y: float, radius: float) -> None:
        self.x = x
        self.y = y
        self.radius = radius

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value: float) -> None:
        if not isinstance(value, (float, int)):
            raise TypeError(f"x must be a float or int not, {type(value)}")
        self._x = value

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value: float) -> None:
        if not isinstance(value, (float, int)):
            raise TypeError(f"y must be a float or int, not {type(value)}")
        self._y = value

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        if not isinstance(value, (float, int)):
            raise TypeError(f"radius must be a float or int, not {type(value)}")
        self._radius = value

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
    


    



