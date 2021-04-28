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
        t = ( (p1.x - p2.x) ** 2 ) + ( (p1.y - p2.y) ** 2 )
        return sympy.sqrt(t)

    def distance(self, other):
        t = ( (self.x - other.x) ** 2 ) + ( (self.y - other.y) ** 2 )
        return sympy.sqrt(t)

    # Midpoint of two points
    @classmethod
    def midpoint(p1, p2):
        P = Point( ((p1.x+p2.x)/2) , ((p1.y+p2.y)/2) )
        return P

    def midpoint(self, other):
        P = Point( ((self.x+other.x)/2) , ((self.y+other.y)/2) )
        return P
