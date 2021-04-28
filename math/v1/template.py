#!/usr/bin/env python3
# name_of_file.py

"""
An explanation of the concept/formula.
Each part and it's function:

a + b = b + a
# check_abba(a, b) -> bool
"""

# import other math concepts
# from determiants import determiant2

def check_abba(a, b):
    return (a + b) == (b + a)


if __name__ == "__main__":
    from util import get_vars

    print("a + b = b + a")
    vars = get_vars({
        "a":float,
        "b":float
    })

    print(check_abba(**vars))
