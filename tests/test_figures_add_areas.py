from typing import Any
from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle
from src.figure import Figure
from common.exceptions import FigureError
from common.typings import SquareUnit

import pytest



@pytest.mark.positive
@pytest.mark.parametrize(
    ("figure_1", "figure_2", "area_summary"),
    [
        (Triangle(3, 5, 7), Square(7), 55.49519052838329),
        (Rectangle(3, 5),  Circle(4), 65.26548245743669),
        (Square(7), Rectangle(3, 5), 64),
        (Circle(4), Triangle(3, 5, 7), 56.76067298581998),
    ],
    ids=[
        "triangle_square",
        "rectangle_circle",
        "square_rectangle",
        "triangle_circle",
    ]
)
def test_circle_area_add_positive(cache, figure_1, figure_2, area_summary):
    assert figure_1.add_area(figure_2) == area_summary,\
        (f"Areas summary for figure_1 {figure_1} and figure_2 {figure_2} "
         f"must be {area_summary}")


class FakeFigure:
    def __init__(self, fake_area):
        self.fake_area = fake_area

    def area(self) -> Any:
        """Return fake area."""
        return self.fake_area



@pytest.mark.parametrize(
    ("figure", "not_figure"),
    [
        (Triangle(3, 5, 7), 7),
        (Rectangle(3, 5), 65.5),
        (Square(7), '1'),
        (Circle(4), 0,),
        (Circle(4), FakeFigure(1)),
    ],
    ids=[
        "triangle_integer",
        "rectangle_float",
        "square_string",
        "circle_zero",
        "circle_fake_int",
    ]
)
def test_circle_area_add_negative(cache, figure, not_figure):
    with pytest.raises(FigureError):
        figure.add_area(not_figure)
