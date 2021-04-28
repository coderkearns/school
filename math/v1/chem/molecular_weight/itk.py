#!/usr/bin/env python3
# chem_mw-from-i-t-k.py

"""MW from i, t, and k:

t = i*((mass/MW)/kg)*k
MW = i*((mass/t)/kg)*k

t(b) = boil_after_change - old_boil
t(f) = freeze_after_change - old_freeze

"""

def calc_mw(temp_after_change, old_temp, k, mass, kg, i):
    t = temp_after_change - old_temp
    return i * k * ( (mass / t) / kg )



if __name__ == "__main__":
    from util import get_vars

    print("MW = i * ( ( mass / t ) / kg ) * k")
    print("t(b) = boil_after_change - old_boil")
    print("t(f) = freeze_after_change - old_freeze")
    print("k = k(b) or k(f), depending on  what was used in t")

    vars = get_vars({
        "temp_after_change":float,
        "old_temp":float,
        "k":float,
        "mass":float,
        "kg":float,
        "i":float
    })

    print(calc_mw(**vars))
