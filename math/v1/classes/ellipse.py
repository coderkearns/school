#!/usr/bin/env python3
# classes/name_of_file.py

doc = """
## Ellipse
The set of all points in a plane where the sum of the distances from two special points, called focus points, is equal.

Every ellipse has two axes of symmetry. The parts of the axes of symmetry which lie inside the ellipse are called the major and minor axes.

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
If `b > a`: This is a `vertical` ellipse.
If `a > v`: This is a `horizontal` ellipse.


"""
__doc__ = doc
__all__ = ["__doc__", "Ellipse"]


import sympy
import json
from util import newerror
from .point import Point
from .line import Line

EllipseException = newerror("EllipseException")

class Ellipse():
    __doc__ = doc

    def __init__(self, major_axis_1, major_axis_2, focus_point_1, focus_point_2, center):
        self.major_axis = Line(major_axis_1, major_axis_2)
        self.focus1 = focus_point_1
        self.focus2 = focus_point_2
        self.center = center

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

    def __repr__(self):
        print(self.equation)
        return f"{self.__class__.__name__}(a={self.a}, b={self.b}, c={self.c}, h={self.h}, k={self.k})"


class HorizontallEllipse(Ellipse):
    doc = __doc__
    def __init__(self, *args):
        super().__init__(*args)

    @property
    def equation(self):
        return f"""
        (x - {self.h})^2    (y - {self.k})^2
        —————————— + —————————— = 1
           {self.a**2}          {self.b**2}
        """


class VerticalEllipse(Ellipse):
    doc = __doc__
    def __init__(self, *args):
        super().__init__(*args)

    @property
    def equation(self):
        return f"""
        (x - {self.h})^2    (y - {self.k})^2
        —————————— + —————————— = 1
           {self.b**2}          {self.a**2}
        """
