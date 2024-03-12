from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    def __init__(self, shape_type) -> None:
        super().__init__()
        self.shape_type = shape_type

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__("circle")
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, height, width) -> None:
        super().__init__("rectangle")
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width


class Square(Shape):
    def __init__(self, side) -> None:
        super().__init__("square")
        self.side = side

    def calculate_area(self):
        return self.side**2
