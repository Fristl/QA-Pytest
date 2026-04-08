from typing import Any

import pytest

from common.exceptions import SizeError
from common.typings import Number
from common.typings import SquareUnit
from src.figures.rectangle import Rectangle


@pytest.mark.positive
@pytest.mark.parametrize(
    ("width", "height", "area"),
    [
        (3, 5, 15),
        (3.5, 6.7, 23.45),
        (4, 7.7, 30.8),
        (4.54, 7, 31.78),
    ],
    ids=["integer", "float", "integer_float", "float_integer"],
)
def test_rectangle_area_positive(
    cache: Any,
    width: Number,
    height: Number,
    area: SquareUnit,
) -> None:
    rectangle = Rectangle(width, height)
    assert rectangle.area == area,\
        f"Rectangle area with sides {width} and {height} must be {area}"


@pytest.mark.parametrize(
    ("width", "height"),
    [
        (12, -5),
        (-12, 5),
        (3.5, -6.7),
        (-3.5, 6.7),
        (-3.5, -6),
        (0, 0),
        (0, 4),
        (0, -7),
    ],
    ids=[
        "integer_positive_negative",
        "integer_negative_positive",
        "float_positive_negative",
        "float_negative_positive",
        "float_integer_negative",
        "zero_zero",
        "zero_integer_positive",
        "zero_integer_negative",
    ],
)
def test_rectangle_negative(cache: Any, width: Number, height: Number) -> None:
    with pytest.raises(SizeError):
        Rectangle(width, height)


@pytest.mark.positive
@pytest.mark.parametrize(
    ("width", "height", "perimeter"),
    [
        (5, 4, 18),
        (1.6, 5.4, 14),
        (10, 6.7, 33.4),
        (9.21, 4, 26.42),
    ],
    ids=["integer", "float", "integer_float", "float_integer"],
)
def test_rectangle_perimeter_positive(
    cache: Any,
    width: Number,
    height: Number,
    perimeter: Number,
) -> None:
    rectangle = Rectangle(width, height)
    assert rectangle.perimeter == perimeter, \
        (
            f"Rectangle perimeter with sides {width} and {height} "
            f"must be {perimeter}",
        )
