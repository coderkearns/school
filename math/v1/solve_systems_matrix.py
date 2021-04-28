#!/usr/bin/env python3
# solve_systems_matrix.py

"""Solve systems using matrices:
ax + by = c
dx + ey = f


Convert to matrices
A = [a b] // coefficents
    [d e]

B = [x]   // variables
    [y]

C = [c]   // equals
    [f]
# make_matrices(a, b, c, d, e, f) -> (A, B, C)


Order equation
[a b] * [x] = [c]
[d e]   [y]   [f]
// A  *  B  =  C


Create Inverse
iA * A * B = iA * C
// B = iA * C

Solve
[x] = [ansX]
[y]   [ansY]
# multiply(iA, C) -> listmatrix[x, y]
"""

from identity_matrix import inverse_matrix

def make_matrices(a, b, c, d, e, f):
    A = [a, b, d, e]
    B = [["x"], ["y"]]
    C = [[c], [f]]
    return A, B, C

def multiply(iA, C):
    return [
        (iA[0]*C[0][0])+(iA[1]*C[1][0]),
        (iA[2]*C[0][0])+(iA[3]*C[1][0])
    ]


if __name__ == "__main__":
    from util import get_vars

    print("ax + by = c\ndx + ey = f")
    vars = get_vars({
        "a":float,
        "b":float,
        "c":float,
        "d":float,
        "e":float,
        "f":float
    })

    A, B, C = make_matrices(**vars)
    iA = inverse_matrix(*A)
    ans = multiply(iA, C)
    print(f"x= {ans[0]}\ny= {ans[1]}")
