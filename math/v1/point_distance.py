#!/usr/bin/env python3
# point_distance.py

"""(
The distance between two points:

D = √( (x1 - x2)^2 + (y1-y2)^2 )

# distance(x1,y1,x2,y2) -> str
"""

from util import strip_float
from math import sqrt

def distance(x1,y1,x2,y2):
    x = (x1 - x2) ** 2
    y = (y1 - y2) ** 2
    t = x + y
    D = strip_float(sqrt(t))
    if type(D) == float:
        D = f"D = √({strip_float(t)})\nD = {D}"
    else:
        D = f"D = {D}"
    return D


if __name__ == "__main__":
    from util import get_vars

    print("D = √( (x1 - x2)^2 + (y1-y2)^2 )")
    vars = get_vars({
        "x1":float,
        "y1":float,
        "x2":float,
        "y2":float
    })

    print(distance(**vars))
