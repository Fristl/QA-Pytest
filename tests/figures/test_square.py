from typing import Any

import pytest

from common.exceptions import SizeError
from common.typings import Number
from common.typings import SquareUnit
from src.figures.square import Square


@pytest.mark.positive
@pytest.mark.parametrize(
    ("side", "area"),
    [
        (5, 25),
        (3.5, 12.25),
    ],
    ids=["integer", "float"],
)
def test_square_area_positive(
    cache: Any,
    side: Number,
    area: SquareUnit,
) -> None:
    square = Square(side)
    assert square.area == area, f"Square area with side {side} must be {area}"


@pytest.mark.parametrize(
    "side",
    [-5, -3.5, 0],
    ids=["integer_negative", "float_negative", "zero"],
)
def test_square_negative(cache: Any, side: Number) -> None:
    with pytest.raises(SizeError):
        Square(side)


@pytest.mark.positive
@pytest.mark.parametrize(
    ("side", "perimeter"),
    [
        (5, 20),
        (1.6, 6.4),
    ],
    ids=["integer", "float"],
)
def test_square_perimeter_positive(
    cache: Any,
    side: Number,
    perimeter: Number,
) -> None:
    square = Square(side)
    assert square.perimeter == perimeter, \
        f"Square perimeter with side {side} must be {perimeter}"
