#!/usr/bin/env python3
# point_distance.py

"""(
The midpoint of two points:

x = (x1+x2)/2
y = (y1+y2)/2
midpoint = (x, y)


# midpoint(x1,y1,x2,y2) -> str
"""

from util import strip_float

def midpoint(x1,y1,x2,y2):
    x = (x1+x2)/2
    y = (y1+y2)/2
    midpoint = f"midpoint = ( {strip_float(x)}, {strip_float(y)} )"
    return midpoint


if __name__ == "__main__":
    from util import get_vars

    print("midpoint = ( (x1+x2)/2 , (y1+y2)/2 )")
    vars = get_vars({
        "x1":float,
        "y1":float,
        "x2":float,
        "y2":float
    })

    print(midpoint(**vars))
