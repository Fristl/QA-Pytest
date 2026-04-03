from typing import Any

import pytest

from common.exceptions import SizeError
from common.typings import Number
from common.typings import SquareUnit
from src.triangle import Triangle
from src.triangle import TriangleError


@pytest.mark.positive
@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c", "area"),
    [
        (3, 5, 7, 6.49519052838329),
        (3.5, 6.7, 8, 11.598896499236465),
        (4, 7.7, 6, 11.86079650571579),
        (4.54, 7, 6.6, 14.493937822068926),
    ],
    ids=["integer", "float", "integer_float_integer", "float_integer_float"],
)
def test_triangle_area_positive(
    cache: Any,
    side_a: Number,
    side_b: Number,
    side_c: Number,
    area: SquareUnit,
) -> None:
    triangle = Triangle(side_a, side_b, side_c)
    assert triangle.area == area,\
        f"Triangle area with sides {side_a}, {side_b}, {side_c} must be {area}"


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c"),
    [
        (12, -5, 10),
        (-12, 5, 3),
        (3.5, -6.7, 5),
        (-3.5, 6.7, 6.6),
        (-3.5, -6, -9),
        (0, 0, 0),
        (0, 4, 10),
        (0, -7, 0.6),
    ],
    ids=[
        "integer_positive_negative_positive",
        "integer_negative_positive_positive",
        "float_positive_negative_positive",
        "float_negative_positive_positive",
        "float_integer_negative",
        "zero",
        "zero_integer_positive",
        "zero_integer_negative_float_positive",
    ],
)
def test_triangle_negative(
    cache: Any,
    side_a: Number,
    side_b: Number,
    side_c: Number,
) -> None:
    with pytest.raises(SizeError):
        Triangle(side_a, side_b, side_c)


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c"),
    [
        (3, 5, 71),
        (3.5, 6.7, 0.8),
        (4, 7.7, 1),
        (4.54, 73, 6.6),
    ],
    ids=["integer", "float", "integer_float_integer", "float_integer_float"],
)
def test_triangle_not_exist(
    cache: Any,
    side_a: Number,
    side_b: Number,
    side_c: Number,
) -> None:
    with pytest.raises(TriangleError):
        Triangle(side_a, side_b, side_c)


@pytest.mark.positive
@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c", "perimeter"),
    [
        (3, 5, 7, 15),
        (3.5, 6.3, 8, 17.8),
        (4, 7.1, 6, 17.1),
        (4.54, 6, 6.6, 17.14),
    ],
    ids=["integer", "float", "integer_float_integer", "float_integer_float"],
)
def test_triangle_perimeter_positive(
    cache: Any,
    side_a: Number,
    side_b: Number,
    side_c: Number,
    perimeter: Number,
) -> None:
    triangle = Triangle(side_a, side_b, side_c)
    assert triangle.perimeter == perimeter,\
        (
            f"Triangle perimeter with sides {side_a}, {side_b}, {side_c}"
            f" must be {perimeter}",
        )
