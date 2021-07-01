#!/usr/bin/env python3
# classes/name_of_file.py

doc = """
## Parabola!

"""
__doc__ = doc
__all__ = ["__doc__", "Parabola", "VertexParabola", "VerticalVertexParabola", "HorizontalVertexParabola"]


import sympy
import json
from util import newerror
from point import Point

def jsoncls(o):
    if hasattr(o, "json"):
        return o.__json__()
    return o.__dict__

ParabolaException = newerror("ParabolaException")

class Parabola():
    __doc__ = doc


class VertexParabola(Parabola):
    def __init__(self, a, *, h=None, k=None):
        if a == 0:
            raise ParabolaException("'a' must not be 0.")
        self.a = a
        self.h = h
        self.k = k

    @property
    def vertex(self):
        return Point(self.h, self.k)
    @property
    def latus_rectum_length(self):
        return abs(1/ self.a)
    @property
    def data(self):
        return {
            "equation": self.equation,
            "direction": self.direction,
            "vertex": self.vertex,
            "axis": self.axis,
            "focus": self.focus,
            "directrix": self.directrix,
            "latus_rectum_length": self.latus_rectum_length
        }

    def __repr__(self):
        r = "\n".join(f"{k}:\t{v}" for k, v in self.data.items())
        print(r)
        return ""
    def __call__(self):
        return json.dumps(self.data, indent=2, default=jsoncls)


class VerticalVertexParabola(VertexParabola):
    def __init__(self, a, h, k):
        VertexParabola.__init__(self, a, h=h, k=k)

    @property
    def equation(self):
        return f"y = {self.a}(x - {self.h})^2 + {self.k}"#.replace("- -", "+ ").replace("+ -", "- ")
    @property
    def direction(self):
        if self.a > 0: return "up"
        return "down"
    @property
    def axis(self):
        return f"x = {self.h}"
    @property
    def focus(self):
        x = self.h
        y = self.k + (1/(4*self.a))
        return Point(x, y)
    @property
    def directrix(self):
        d = self.k - (1/ (4*self.a))
        return f"y = {d}"



class HorizontalVertexParabola(VertexParabola):
    def __init__(self, a, k, h):
        VertexParabola.__init__(self, a, k=k, h=h)

    @property
    def equation(self):
        return f"x = {self.a}(y - {self.k})^2 + {self.h}"#.replace("- -", "+ ").replace("+ -", "- ")
    @property
    def direction(self):
        if self.a > 0: return "right"
        return "left"
    @property
    def axis(self):
        return f"y = {self.k}"
    @property
    def focus(self):
        x = self.h + (1/ (4*self.a))
        y = self.k
        return Point(x, y)
    @property
    def directrix(self):
        d = self.h - (1/ (4*self.a))
        return f"x = {d}"
