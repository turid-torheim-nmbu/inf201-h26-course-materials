import math


class Circle:
    """Circle shape."""

    def __init__(self, center: int | float, radius: int | float) -> None:
        """
        center: coordinates of circle center
        radius: radius of circle (>= 0 required)
        """

        assert radius >= 0, "Radius must be strictly positive"
        self.ctr = center
        self.rad = radius

    def area(self) -> float:
        """Area of circle."""
        return math.pi * self.rad**2


class Rectangle:
    def __init__(self, lower_left: tuple[int | float, int | float], upper_right: tuple[int | float, int | float]) -> None:
        """Create rectangle based on lower left and upper rigth coordinates"""
        self.ll = lower_left
        self.ur = upper_right

    def area(self) -> int | float:
        """Calculates the area of the rectangle"""
        return (self.ur[0] - self.ll[0]) * (self.ur[1] - self.ll[1])
