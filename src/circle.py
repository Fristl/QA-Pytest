"""Module with a circle figure."""

from math import pi

from common.typings import Number
from common.typings import SquareUnit
from src.figure import Figure


class Circle(Figure):
    """Circle figure base class."""

    def __init__(self, radius: Number):
        self._radius = super().check_size(radius)
        self._diameter = self._radius * 2

    def _area(self) -> SquareUnit:
        """Calculate the area of the figure."""
        return pi * (self._radius ** 2)

    def _perimeter(self) -> Number:
        """Calculate the perimeter of the figure."""
        return pi * self._diameter
