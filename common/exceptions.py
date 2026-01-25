"""Module with specific exceptions."""

from typing import Any

from common.typings import Number


__all__ = [
    "FigureError",
    "SizeError",
    "TriangleError",
]

class SizeError(ValueError):
    """Size value error."""

    MESSAGE = "Size with value: %s is invalid"

    def __init__(self,  size: Number, message: str = MESSAGE):
        super().__init__(message % size)


class TriangleError(ValueError):
    """Triangle doesn't exist."""

    MESSAGE = "Triangle with sides: %s, %s, %s doesn't exist."

    def __init__(
        self,
        size_a: Number,
        size_b: Number,
        size_c: Number,
        message: str = MESSAGE,
    ):
        super().__init__(message % (size_a, size_b, size_c))


class FigureError(TypeError):
    """Error show that it is not Figure instance."""

    MESSAGE = "Object %s with type %s is not a Figure instance."

    def __init__(self, figure: Any, message: str = MESSAGE):
        super().__init__(message % (figure, type(figure)))
