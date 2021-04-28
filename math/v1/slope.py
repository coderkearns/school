#!/usr/bin/env python3
# slope.py

"""Slope:

m = rise / run

rise = y2 - y1
run = x2 - x1

if x1 == x2:
    line is vertical
    slope = "undefined" (None)

if y1 == y2:
    line is horizontal
    slope = 0.0

# checkslope(x1, y1, x2, y2) -> [float or None or False]
# slope(x1, y1, x2, y2) -> float
"""

def checkslope(x1, y1, x2, y2):
    if x1 == x2:
        return None
    if y1 == y2:
        return 0
    return True

def slope(x1, y1, x2, y2):
    check = checkslope(x1, y1, x2, y2)
    if check != True:
        return check
    rise = y2 - y1
    run = x2 - x1
    return rise / run


if __name__ == "__main__":
    from util import get_vars

    print("m = (y2-y1) / (x2-x1)")
    vars = get_vars({
        "x1":float,
        "y1":float,
        "x2":float,
        "y2":float
    })

    print(slope(**vars))
