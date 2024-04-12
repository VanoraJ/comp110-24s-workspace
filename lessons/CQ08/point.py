"""CQ08 - Creating Point Class."""

from __future__ import annotations

__author__ = "730653557"


class Point:
    """Creating the Point class."""

    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Defining the constructor of Point."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """The mutating method."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """The non-mutating method, creating a new Point."""
        new_x: float = self.x * factor
        new_y: float = self.y * factor
        new_point: Point = Point(new_x, new_y)\
        
        return new_point