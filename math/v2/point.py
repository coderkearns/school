#!/usr/bin/env python3
# classes/name_of_file.py

doc = """
## Point(x, y)

### Each of the following are both a classmethod and instancemethod
distance = √( (x1 - x2)^2 + (y1-y2)^2 )
midpoint = ( (x1+x2)/2 , (y1+y2)/2 )

"""
__doc__ = doc

import sympy

__all__ = ["__doc__", "Point"]

class Point():
    __doc__ = doc

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def json(self):
        return f"({self.x}, {self.y})"

    # Distance between two points
    @classmethod
    def distance(p1, p2):
        t = ((p1.x - p2.x)**2) + ((p1.y - p2.y)**2)
        return sympy.sqrt(t)

    def distance(self, other):
        t = ((self.x - other.x)**2) + ((self.y - other.y)**2)
        return sympy.sqrt(t)

    # Midpoint of two points
    @classmethod
    def midpoint(p1, p2):
        P = Point(((p1.x+p2.x)/2), ((p1.y+p2.y)/2))
        return P

    def midpoint(self, other):
        P = Point(((self.x+other.x)/2), ((self.y+other.y)/2))
        return P

    def as_dict(self):
        return {"x": self.x, "y": self.y}

    def as_tuple(self):
        return (self.x, self.y)

    def as_list(self):
        return [self.x, self.y]


def toPoint(*args, **kwargs):
    # If using kwargs: toPoint(x=1, y=5)
    if "x" in kwargs.keys() and "y" in kwargs.keys():
        return Point(kwargs["x"], kwargs["y"])

    # If unpacking or using multiple args:
    # toPoint(1, 5)
    # toPoint(*[1, 5])
    if len(args) > 1:
        return Point(args[0], args[1])

    # If empty: toPoint()
    if len(args) == 0:
        return Point(0, 0)

    # If only one argument: toPoint(something_or_other)
    # Then, use in the following...
    item = args[0]

    # If given Point: toPoint(Point(1, 5))
    if isinstance(item, Point):
        return item

    # If given dict: toPoint({"x": 1, "y": 5})
    if type(item) == dict:
        return Point(item["x"], item["y"])

    # If list or tuple
    return Point(item[0], item[1])