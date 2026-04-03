from src.square import Square
from common.exceptions import SizeError
import pytest


@pytest.mark.positive
@pytest.mark.parametrize(
    ("side", "area"),
    [
        (5, 25),
        (3.5, 12.25),
    ],
    ids=["integer", "float"]
)
def test_square_area_positive(cache, side, area):
    square = Square(side)
    assert square.area == area, f"Square area with side {side} must be {area}"


@pytest.mark.parametrize(
    "side",
    [-5, -3.5, 0],
    ids=["integer_negative", "float_negative", "zero"],
)
def test_square_negative(cache, side):
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
def test_square_perimeter_positive(cache, side, perimeter):
    square = Square(side)
    assert square.perimeter == perimeter, \
        f"Square perimeter with side {side} must be {perimeter}"
