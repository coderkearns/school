#!/usr/bin/env python3
# classes/name_of_file.py

doc = """
## Line(p1, p2)
"""
__doc__ = doc

from .point import Point
from util import newerror

__all__ = ["__doc__", "Line", "LineError"]

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
                raise LineError("Argument must be a Point, list, or tuple")

    @property
    def length(self):
        return Point.distance(self.p1, self.p2)

    def __repr__(self):
        return f"Line( {self.p1} -> {self.p2} )"
