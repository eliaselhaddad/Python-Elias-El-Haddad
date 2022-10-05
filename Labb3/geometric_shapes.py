from math import pi

class Circle:

    def __init__(self, x: float, y: float, r: float) -> None:
        self.x = x
        self.y = y
        self.r = r

    @property
    def area(self):
        return pi*self.r**2