#!/usr/bin/env python3
# vertex_form.py

"""Vertex Quadratic Formula

y = a(x-h)^2 + k

line of symetry = h
vertex = (h, k)
y-intercept = ( a*(0-h)^2 + k )

# vertex(h, k) -> str
# y_intercept(a, h, k) -> float

# vertex_form(a, h, k) -> str

# format_func(a, h, k)

"""

from math import sqrt
from util import strip_all
from problems_with_quadratics import convert_to_point

def format_func(a, h, k):
    a,h,k = strip_all(a,h,k)
    return f"y = {a}(x - {h})^2 + {k}".replace("- -", "+ ")

def vertex(h, k):
    return convert_to_point(h, k)

def y_intercept(a, h, k):
    return ( a*(0.0 - h)**2 + k)

def vertex_form(a, h, k):
    func = format_func(a, h, k)

    los = h
    v = vertex(h, k)
    y = y_intercept(a, h, k)

    los, y = strip_all(los,y)
    los, v, y = map(str, (los,v,y))

    return "\n".join([
        func,
        "",
        "line of symmetry = "+los,
        "vertex = "+v,
        "y-intercept = "+y
    ])


if __name__ == "__main__":
    from util import get_vars

    print("y = a(x-h)^2 + k")
    vars = get_vars({
        "a":float,
        "h":float,
        "k":float
    })

    print()
    print(vertex_form(**vars))
