from src.circle import Circle
from common.exceptions import FigureError
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


@pytest.mark.positive
@pytest.mark.parametrize(
    ("radius_1", "radius_2", "summary_area"),
    [
        (11, 3, 408.40704496667314),
        (11, 3.3, 414.34465508195785),
        (11.9, 3, 473.1552695571588),
        (11.7, 3.7, 473.061021777551),
    ],
    ids=[
        "integer_integer",
        "integer_float",
        "float_integer",
        "float_float",
    ],
)
def test_circle_area_add_positive(cache, radius_1, radius_2, summary_area):
    circle_1 = Circle(radius_1)
    circle_2 = Circle(radius_2)
    assert circle_1.add_area(circle_2) == summary_area,\
        (
            f"Areas summary with circles with radius {radius_1} and "
            f"{radius_2} must be {summary_area}"
        )


@pytest.mark.parametrize(
    ("circle", "not_figure"),
    [
        (Circle(11), 3),
        (Circle(11), 3.5),
        (Circle(11), "1"),
        (Circle(11), 0),
    ],
    ids=[
        "integer",
        "float",
        "string",
        "zero",
    ],
)
def test_circle_area_add_negative(cache, circle, not_figure):
    with pytest.raises(FigureError):
        circle.add_area(not_figure)
