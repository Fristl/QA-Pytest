"""Module with a rectangle figure."""

from common.typings import Number
from common.typings import SquareUnit
from src.figure import Figure


class Rectangle(Figure):
    """Rectangle figure base class."""

    def __init__(self, width: Number, height: Number):
        self._width = super().check_size(width)
        self._height = super().check_size(height)

    def _area(self) -> SquareUnit:
        """Calculate the area of the figure."""
        return self._width * self._height

    def _perimeter(self) -> Number:
        """Calculate the perimeter of the figure."""
        return (self._width + self._height) * 2
