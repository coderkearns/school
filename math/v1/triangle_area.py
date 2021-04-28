#!/usr/bin/env python3
# triangle_area.py

"""Triangle Area:
Constructing triangle area using 3 points and determiants.

Using points: (a, b), (c, d), and (e, f)

             | a b 1 |
A = (1/2)*abs(| c d 1 |)
             | e f 1 |
# triangle_area(a,b,c,d,e,f) -> float

"""

from determiants import determiant3

def triangle_area(a,b,c,d,e,f):
    return ( (1/2)*abs(determiant3(a, b, 1, c, d, 1, e, f, 1)) )


if __name__ == "__main__":
    from util import get_vars

    print("Points (a, b), (c, d), and (e, f)")
    vars = get_vars({
    "a":float,
    "b":float,
    "c":float,
    "d":float,
    "e":float,
    "f":float
    })

    print(triangle_area(**vars))
