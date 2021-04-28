#!/usr/bin/env python3
# determiants.py

"""Determiant:
A square matrix.

| a b | = ad - bc
| c d |
"""

from determiants import determiant2

if __name__ == "__main__":
    from util import get_vars

    print("|a b, c d| =\nad - bc")
    vars = get_vars({
        "a":float,
        "b":float,
        "c":float,
        "d":float
    })

    print(determiant2(**vars))
