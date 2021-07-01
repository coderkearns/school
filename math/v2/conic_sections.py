#!/usr/bin/env python3

doc = """
## Conic Sections

All circles, ellipses, hyperbolas, and parabolas are conic sections.
They all share the same equation, so it can be difficult to tell the apart.
We use discriminants to tell the apart from one another.

### Equation of a Conic Section

The equation for a conic section is:
```
Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0
```
where `A`, `B`, and `C` are not all 0.

### Discriminants

The discriminant of a conic section (using the above formula) can be calculated by using:
```
d = B^2 - 4AC
```
From there, you can tell the type of conic section using this table:
| Conic Section | Discriminant |
| ------------- | ------------ |
| Parabola      | `d = 0`      |
| Hyperbola     | `d > 0`      |
| Circle        | `d < 0, B = 0, A = C` |
| Ellipse       | `d < 0, B != 0` |
| Ellipse       | `d < 0, A != 0, C != 0, A != C` |

### Class Info

`::__init__(A, B, C, D, E, F)` <br/>
Create a new ConicSection. <br/>
A, B, C, D, E, and F are the same as in the equation.

`::discrimiant` <br/>
A property, which calulates the discrimiant. <br/>
It uses `B^2 - 4AC`

`::type` <br/>
Get the type of Conic Section. <br/>
It uses the table listed above, and return the class for that type of conic section.
"""
__doc__ = doc

from util import newerror
ConicSectionException = newerror("ConicSectionException")


from parabola import Parabola
from hyperbola import Hyperbola
from circle import Circle
from ellipse import Ellipse



class ConicSection():
    __doc__ = doc

    def __init__(self, A, B, C, D, E, F):
        if (A == 0 and B == 0 and C == 0): raise ConicSectionException("A, B, and C cannot all be 0")

        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.E = E
        self.F = F

    @property
    def discriminant(self):
        return (self.B**2) - (4 * self.A * self.C)

    @property
    def type(self):
        d = self.discriminant

        if d == 0: return Parabola
        if d > 0: return Hyperbola
        if d < 0:
            if (self.B == 0 and self.A == self.C): return Circle
            if (self.B != 0): return Ellipse
            if (self.A != 0 and self.C != 0 and self.A != self.C): return Ellipse

        raise ConicSectionException("Not a Parabola, Hyperbola, Circle, or Ellipse")


def main(A, B, C, D, E, F):
    conic_section = ConicSection(A, B, C, D, E, F)
    print(conic_section.type.__name__)

if __name__ == '__main__':
    from util import get_vars

    print("Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0")

    main(**get_vars({
        "A": float,
        "B": float,
        "C": float,
        "D": float,
        "E": float,
        "F": float,
    }))
