"""Module with a square figure."""

from common.typings import Number
from src.rectangle import Rectangle


class Square(Rectangle):
    """Square figure base class."""

    def __init__(self, side: Number):
        super().__init__(side, side)
