from math import pi

class Circle:

    def __init__(self, x: float, y: float, r: float) -> None:
        self.x = x
        self.y = y
        self.r = r

    @property
    def area(self):
        return pi*self.r**2

    @property
    def circumference(self):
        return 2*pi*self.r

    def __eq__(self, other) -> bool:
        if self.area == other.area:
            return True
        else:
            return False

    



