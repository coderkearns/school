#!/usr/bin/env python3
# cramers_rule2.py

"""
When solving system: ax + by = c
                     dx + ey = f
# get_vars() -> {a,b,c,d,e,f}


if: |a b| ≠ 0
    |d e|
# condition_one(a,b,d,e) -> bool


x = |c b|  / |a b|
    |f e| /  |d e|
# ans_x(a,b,c,d,e,f) -> float


y = |a c|  / |a b|
    |d f| /  |d e|

# ans_y(a,b,c,d,e,f) -> float
"""

from determiants import determiant2

def condition_one(a,b,d,e):
    d = determiant2(a, b, d, e)
    return d != 0

def ans_x(a, b, c, d, e, f):
    if not condition_one(a,b,d,e): quit("determiant|a b, d e| = 0, none")
    x = determiant2(c, b, f, e) / determiant2(a, b, d, e)
    return x

def ans_y(a, b, c, d, e, f):
    if not condition_one(a,b,d,e): quit("determiant|a b, d e| = 0, none")
    y = determiant2(a, c, d, f) / determiant2(a, b, d, e)
    return y


if __name__ == "__main__":
    from util import get_vars

    print("ax + by = c\ndx + ey = f")
    vars = get_vars({
        "a":float,
        "b":float,
        "c":float,
        "d":float,
        "e":float,
        "f":float,
        })

    x = ans_x(**vars)
    y = ans_y(**vars)

    print(f"x = {x}")
    print(f"y = {y}")
