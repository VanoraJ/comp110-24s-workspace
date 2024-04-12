"""CQ08 - making points."""

__author__ = "730653557"

from lessons.CQ08.point import Point

my_point1: Point = Point(2, 4)

my_point1.scale_by(2)
print(my_point1.x, my_point1.y)

my_point2: Point = Point(2, 4)
modified_point = my_point2.scale(2)
print(my_point2.x, my_point2.y)
print(modified_point.x, modified_point.y)