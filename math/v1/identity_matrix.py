#!/usr/bin/env python3
# identity_matrix.py

"""
Identity Matrix:
a * 1 = 1

[a b] * [1 0] = [a b]
[c d]   [0 1]   [c d]


Inverse Matrix:
(a*1)/a=1

A = [a b]
    [c d]

if |a b| ≠ 0
   |c d|
# condition_one(a, b, c, d) -> bool

I = 1/(|a b|)*[d -b]
       |c d|  [-c a]
# inverse_matrix(a,b,c,d) -> ListMatrix[[a, b],[c, d]]
"""


from determiants import determiant2

def condition_one(a, b, c, d):
    return determiant2(a, b, c, d) != 0

def inverse_matrix(a, b, c, d):
    if not condition_one(a,b,c,d): quit("|a b, c d| == 0, none")
    multiplier = (1/determiant2(a,b,c,d))
    a *= multiplier
    b *= multiplier
    c *= multiplier
    d *= multiplier
    return (d, -1*(b), -1*(c), a)

def print_matrix(a, b, c, d):
    print(f"[{a}  {b}]\n[{c}  {d}]")

if __name__ == "__main__":
    from util import get_vars

    print("A = [a b]\n    [c d]")
    vars = get_vars({
        "a":float,
        "b":float,
        "c":float,
        "d":float,
    })

    print_matrix(*inverse_matrix(**vars))
