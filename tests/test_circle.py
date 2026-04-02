from src.circle import Circle
from common.exceptions import SizeError
import pytest


@pytest.mark.positive
@pytest.mark.parametrize(
    ("radius", "area"),
    [
        (11, 380.132711084365),
        (3.1, 30.190705400997917),
    ],
    ids=["integer", "float"]
)
def test_circle_area_positive(cache, radius, area):
    circle = Circle(radius)
    assert circle.area == area,\
        f"Circle area with radius {radius} must be {area}"


@pytest.mark.parametrize(
    "radius",
    [-12, -3.5, 0],
    ids=["integer_negative", "float_negative", "zero"]
)
def test_circle_negative(cache, radius):
    with pytest.raises(SizeError):
        Circle(radius)


@pytest.mark.positive
@pytest.mark.parametrize(
    ("radius", "perimeter"),
    [
        (2, 12.566370614359172),
        (5.7, 35.814156250923645),
    ],
    ids=["integer", "float"]
)
def test_circle_perimeter_positive(cache, radius, perimeter):
    circle = Circle(radius)
    assert circle.perimeter == perimeter,\
        f"Circle perimeter with radius {radius} must be {perimeter}"
