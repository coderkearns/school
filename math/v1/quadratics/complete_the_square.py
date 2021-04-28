#!/usr/bin/env python3
# complete_the_square.py

"""Complete the Square:

a*(x**2) + b*x + c = 0

d = b / (2*a)
e = -1 * ( c - ((b**2) / (4*a)) )

a*(x + d)**2 = e

# complete_the_square(a,b,c) -> str
"""

def complete_the_square(a, b, c):
    d = b / (2*a)
    e = -1 * ( c - ( (b**2) / (4*a) ) )
    a = a if a != 1 else ""
    return f"{a}(x + {d})^2 = {e}"


if __name__ == "__main__":
    from util import get_vars

    print("ax^2 + bx + c = 0")
    vars = get_vars({
        "a":float,
        "b":float,
        "c":float
    })

    print(complete_the_square(**vars))
