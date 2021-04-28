#!/usr/bin/env python3

doc = """
## Line


`::__init__(p1, p2)`
* `p1`: The start point, in the form of a Point, a tuple, or a list
* `p2`: The end point, in the same form as `p1`


`.length`
* Calculates the length of the line

"""
__doc__ = doc

from point import Point
from util import newerror

__all__ = ["__doc__", "Line", "LineException"]

LineException = newerror("LineException")

class Line():
    __doc__ = doc

    def __init__(self, p1, p2):
        for i, p in enumerate([p1, p2]):
            if type(p) == Point:
                setattr(self, f"p{i+1}", p)
            elif type(p) in [tuple, list]:
                setattr(self, f"p{i+1}", Point(*p))
            else:
                raise LineException("Argument must be a Point, list, or tuple")

    @property
    def length(self):
        return Point.distance(self.p1, self.p2)

    def __repr__(self):
        return f"Line( {self.p1} -> {self.p2} )"
