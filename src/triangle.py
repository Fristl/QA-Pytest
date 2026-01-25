"""Module with a triangle figure."""

from math import sqrt

from common.exceptions import TriangleError
from common.typings import Number
from common.typings import SquareUnit
from src.figure import Figure


class Triangle(Figure):
    """Triangle figure base class."""

    def __init__(self, side_a: Number, side_b: Number, side_c: Number):
        self._side_a = super().check_size(side_a)
        self._side_b = super().check_size(side_b)
        self._side_c = super().check_size(side_c)

        if not self.__triangle_exist():
            raise TriangleError(self._side_a, self._side_b, self._side_c)


    def __triangle_exist(self) -> bool:
        """Check if triangle exists."""
        return (
            self._side_a + self._side_b > self._side_c and
            self._side_a + self._side_c > self._side_b and
            self._side_b + self._side_c > self._side_a
        )

    def _area(self) -> SquareUnit:
        """Calculate the area of the figure."""
        half_perimeter = self._perimeter() / 2
        return sqrt(
            half_perimeter *
            (half_perimeter - self._side_a) *
            (half_perimeter - self._side_b) *
            (half_perimeter - self._side_c),
        )

    def _perimeter(self) -> Number:
        """Calculate the perimeter of the figure."""
        return self._side_a + self._side_b + self._side_c
