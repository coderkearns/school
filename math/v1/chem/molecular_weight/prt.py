#!/usr/bin/env python3
# chem_mw-from-i-t-k.py

"""MW from p, r, and t:

p = osmotic pressure (Π)
v = liters solution
m = mass solute

MW = r * t * ( ( m / p ) / v )

"""

def calc_mw(m, v, t, p, r):
    tk = t + 273
    return tk * r * ( (m / p) / v )



if __name__ == "__main__":
    from util import get_vars

    print("MW = r * t * ( ( m / p ) / v )")
    print("m = mass solute")
    print("v = liters solution")
    print("t = temperature in C")
    print("p = osmosis pressure (Π)")
    print()
    print("r =\t0.0821\t@ atm,\n\t62.4\t@ torr/mmHg\n\t8.31\t@ kPa")
    print()


    vars = get_vars({
        "m":float,
        "v":float,
        "t":float,
        "p":float,
        "r":float
    })

    print(calc_mw(**vars))
