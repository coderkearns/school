#!/usr/bin/env python3
# quadratic_formula.py

"""The Quadratic Formula

with ax^2 + bx + c = 0
if a != 0


     -b ± sqrt( b^2 - 4ac )
x = -------------------------
             2a


x = ( ( -b ±sqrt( b^2 - ( 4*a*c )) ) / 2a )

# quadratic_formula(a,b,c) -> str

discriminant = b^2 - 4ac

if discriminant > 0: two real roots
if discriminant = 0: one repeated real root
if discriminant < 0: two imaginary roots

# check_discriminant(a,b,c) -> str

"""

from math import sqrt

def check_discriminant(a, b, c):
    d = (b**2) - (4*a*c)
    ans = ""
    if d > 0:   ans = "two real roots"
    if d == 0:  ans = "one repeated real root"
    if d < 0:   ans = "two imaginary roots"
    return (ans, d)

def quadratic_formula(a, b, c):
    d_ans, d = check_discriminant(a,b,c)
    top1, top2, bottom = ("error",)*3

    top1 = -1 * b
    i = False
    try:
        top2 = sqrt( b**2 - (4*a*c) )
    except ValueError:
        e = b**2 - (4*a*c)
        top2 = f"{sqrt(abs(e))}"
        i = True
    if str(top2).split(".")[1] != "0":
        e = (b**2) - (4*a*c)
        top2 = f"√( {e} )"
        try:
            sqrt(e)
        except ValueError:
            i = True
            top2 = f"√( {abs(e)} )"
    bottom = 2*a

    i = "i" if i else ""

    ans = f"x = ( {top1} ± {i}{top2} ) / {bottom}"
    if d == 0:
        ans = f"x = { top1 / bottom }"

    try:
        if d != 0.00:
            ans += f"\nx = {(top1 + top2) / bottom}"
            ans += f"\nx = {(top1 - top2) / bottom}"
    except Exception:
        pass

    return f"d = {d}\n{d_ans}\n{ans}"


if __name__ == "__main__":
    from util import get_vars

    print("ax^2 + bx + c = 0")
    vars = get_vars({
        "a":float,
        "b":float,
        "c":float
    })

    print()
    print(quadratic_formula(**vars))
