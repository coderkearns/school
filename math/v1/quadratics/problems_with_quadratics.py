#!/usr/bin/env python3
# problems_with_quadratics.py

"""Solving Problems with Quadratics:

Creating tables, yay. (sarcastic)

create equation (not done here)
0. turn into function:
# get_f(func: str) -> function
    # f(x) -> float

1. Get a, b, c, and function
2. get vertex x - Line of Symmetry - from a and b: ( x = (-1*b)/(2*a) )
3. solve func with x to get y: f(x)
4. give back vertex: P( x, y )

# line_of_symmetry(a, b) -> float
# convert_to_point(x, y)
# solve_problem_with_quadratics(a, b, c, func)

# format_func(func) -> func
# format_ans(func,los,vertex,y_intercept) -> str

"""

from util import strip_float
from plot import plot

def get_f(a, b, c):
    func=f"{a}*(x)**2 + {b}*x + {c}".replace("x", "{0}").replace("^", "**")
    def f(x):
        return eval(func.format(x))
    return (f, func)

def format_func(func):
    return func.replace("{0}", "x").replace("**","^").replace("*","")

def line_of_symmetry(a, b):
    return (-1*b) / (2*a)

def convert_to_point(x, y):
    return f"( {strip_float(x)}, {strip_float(y)} )"

def solve_problem_with_quadratics(a, b, c, *p, **k):
    f, func = get_f(a, b, c)
    func = format_func(func)

    los = line_of_symmetry(a, b)
    vertex = convert_to_point(los, f(los))
    y_intercept = convert_to_point(0, c)

    return (f,func,los,vertex,y_intercept, [a, b, c])

def create_table(f, x_name, y_name, rows):
    x = len(x_name)
    data = []
    row = 0
    while True:
        spaces = (" "*(x-len(str(row))))
        y = f(row)
        if y < 0: break
        data.append(f"{row}{spaces} | {y}")
        row += 1
    print(x_name + " | " + y_name)
    print("-"*(x+1) + "|" + "-"*(len(y_name)+1) )
    print("\n".join(data))
    return data



def format_ans(func,los,vertex,y_intercept, abc):
    func,los,vertex,y_intercept = map(str, [func,los,vertex,y_intercept])
    return "\n".join([
        "y = "+func,
        "",
        "line of symetry: "+los,
        "vertex: "+vertex,
        "y-intercept: "+y_intercept,
        "",
        "direction: "+("up" if abc[0]>0 else "down"),
        "vertex type: "+("minimum" if abc[0]>0 else "maximum")
    ])

if __name__ == "__main__":
    from util import get_vars

    print("ax^2 + bx + c")
    vars = get_vars({
        "a":float,
        "b":float,
        "c":float,
        "x":str,
        "y":str
    })

    print()
    f,func,l,v,y,abc = solve_problem_with_quadratics(**vars)
    print(format_ans(func,l,v,y,abc))
    print()
    data = create_table(f,vars["x"],vars["y"], 10)
    plot(f, v, data, vars["x"], vars["y"])
