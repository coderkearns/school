#!/usr/bin/env python3
# classes/name_of_file.py

doc = """
## Ellipse

The set of all points in a plane where the sum of the distances from two special points, called focus points or foci, is equal.

Every ellipse has two axes of symmetry. The parts of the axes of symmetry which lie inside the ellipse are called the major and minor axes. The two foci will always lie on the major axis.

### Class

`::__init__`
- `major_axis_1`: the start of th major axis, in the form of a Point
- `major_axis_2`: the end of th major axis, in the form of a Point
- `focus_point_1`: one of the focus points, a Point
- `focus_point_2`: the other focus point, a Point
- `center`: the center of the ellipse, a Point

`.h`: The x of the center point

`.k`: The y of the center point

`.a`: Half the major axis's length

`.c`: Half the distance between the focus points

`.b`: The square root of `a^2 -  c^2`

`.type`: Returns "horizontal" or "vertical"

`.equation`: Returns the equation for the ellipse

### Special Points
The focus points, or foci, lie on the major axis.
Consequently, the major axis is a longer segment whose distance is `2a`, whereas the minor axis is the shorter segment whose distance is `2b(a > b)`.
The distance between the foci is `2c`.
There is a special relationship between `a`, `b` and `c` in an ellipse. self relationship, involving the Pythagorean theorem, is `b^2 = a^2 - c^2`

### Equation
The equation of an ellipse with a horizontal major axis and center `(h, k)` is:
```
(x - h)^2    (y - k)^2
—————————— + —————————— = 1
   a^2          b^2
```

The equation of an ellipse with a vertical major axis and center `(h, k)` is:
```
(x - h)^2    (y - k)^2
—————————— + —————————— = 1
   b^2          a^2
where b^2 = a^2 - c^2
```

### How to tell it's type
`a > b`

"""
__doc__ = doc
__all__ = ["__doc__", "Ellipse", "EllipseException"]

import sympy
import json
from util import newerror, strip_float
from point import Point, toPoint
from line import Line

EllipseException = newerror("EllipseException")


class Ellipse():
    __doc__ = doc

    def __init__(self, major_axis_1, major_axis_2, focus_point_1, focus_point_2, center):
        self.major_axis = Line(toPoint(major_axis_1), toPoint(major_axis_2))
        self.focus1 = toPoint(focus_point_1)
        self.focus2 = toPoint(focus_point_2)
        self.center = toPoint(center)

    def json(self):
        openbrace = "\u007b"
        closebrace = "\u007d"
        return f"{openbrace}'major_axis_1': {self.major_axis.p1.json()}, 'major_axis_2': {self.major_axis.p2.json()}, 'focus1': {self.focus1.json()}, 'focus2': {self.focus2.json()}, 'center': {self.center.json()}{closebrace}"

    @property
    def h(self):
        return self.center.x

    @property
    def k(self):
        return self.center.y

    @property
    def a(self):
        return self.major_axis.length / 2

    @property
    def c(self):
        return self.focus1.distance(self.focus2) / 2

    @property
    def b(self):
        left = (self.a ** 2) - (self.c ** 2)
        b = sympy.sqrt(left)
        return b

    @property
    def type(self):
        if self.b > self.a:
            return "horizontal"
        elif self.a > self.b:
            return "vertical"
        else:
            raise EllipseException("a and b must not be equal!")

    @property
    def equation(self):
        if self.type == "horizontal":
            return f"""
            (x - {self.h})^2    (y - {self.k})^2
            —————————— + —————————— = 1
               {self.a**2}          {self.b**2}
            """
        else:
            return f"""
            (x - {self.h})^2    (y - {self.k})^2
            —————————— + —————————— = 1
               {self.b**2}          {self.a**2}
            """


    def __repr__(self):
        print(self.equation)
        return f"{self.__class__.__name__}(a={self.a}, b={self.b}, c={self.c}, h={self.h}, k={self.k})"


def main(h, k, a, b):
    c = sympy.sqrt(a - b)
    if b > a:
        print(f"({strip_float(h)}, {strip_float(k+c)})")
        print(f"({strip_float(h)}, {strip_float(k-c)})")
    else:
        print(f"({strip_float(h+c)}, {strip_float(k)})")
        print(f"({strip_float(h-c)}, {strip_float(k)})")


if __name__ == '__main__':
    from util import get_vars
    main(**get_vars({
        "h": float,
        "k": float,
        "a": float,
        "b": float
    }))
