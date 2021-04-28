#!/usr/bin/env python3
# cramers_rule3.py

"""
When solving system: a1x + b1y + c1z = d1
                     a2x + b2y + c2z = d2
                     a3x + b3y + c3z = d3
# get_vars() -> {a1,b1,c1,d1,a2,b2,c2,d2,a3,b3,c3,d3}


if: |a b| ≠ 0
    |d e|
# condition_one(a,b,d,e) -> bool


x = |c b|  / |a b|,
    |f e| /  |d e|
# ans_x(a,b,c,d,e,f) -> float


y = |a c|  / |a b|
    |d f| /  |d e|

# ans_y(a,b,c,d,e,f) -> float
"""

from determiants import determiant3

def condition_one(determiant):
    return determiant != 0

def ans_x(a1,b1,c1,d1,a2,b2,c2,d2,a3,b3,c3,d3, determiant):
    if not condition_one(determiant):
        return "none"
    else:
        return determiant3(d1,b1,c1, d2,b2,c2, d3,b3,c3) / determiant
    return x

def ans_y(a1,b1,c1,d1,a2,b2,c2,d2,a3,b3,c3,d3, determiant):
    if not condition_one(determiant):
        return "none"
    else:
        return determiant3(a1,d1,c1, a2,d2,c2, a3,d3,c3) / determiant

def ans_z(a1,b1,c1,d1,a2,b2,c2,d2,a3,b3,c3,d3, determiant):
    if not condition_one(determiant):
        return "none"
    else:
        return determiant3(a1,b1,d1, a2,b2,d2, a3,b3,d3) / determiant

def cramers_rule3(a1,b1,c1,d1,a2,b2,c2,d2,a3,b3,c3,d3):
    d = determiant3(a1,b1,c1, a2,b2,c2, a3,b3,c3)

    x = ans_x(*vars.values(), d)
    y = ans_y(*vars.values(), d)
    z = ans_z(*vars.values(), d)


if __name__ == "__main__":
    from util import get_vars

    print("a1x + b1y + c1z = d1\na2x + b2y + c2z = d2\na3x + b3y + c3z = d3")
    vars = get_vars({
        "a1":float,
        "b1":float,
        "c1":float,
        "d1":float,
        "a2":float,
        "b2":float,
        "c2":float,
        "d2":float,
        "a3":float,
        "b3":float,
        "c3":float,
        "d3":float,
        })

    d = determiant3(vars["a1"],vars["b1"],vars["c1"], vars["a2"],vars["b2"],vars["c2"], vars["a3"],vars["b3"],vars["c3"])

    x = ans_x(*vars.values(), d)
    y = ans_y(*vars.values(), d)
    z = ans_z(*vars.values(), d)


    print()
    print(f"d = {d}")
    print()
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"z = {z}")
