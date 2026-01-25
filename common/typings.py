"""It's module with custom types for project."""

from __future__ import annotations

from typing import Annotated
from typing import Union


__all__ = [
    "Number",
    "SquareUnit",
]


Number = Union[int, float]  # noqa: UP007
SquareUnit = Annotated[Number, "Unit of square"]
