#!/usr/bin/env python3
# chem/osmotic_pressure.py

"""R constant:

used in most equations dealing with pressure, "R" is different for each unit of pressure.

R @:
    atm =   0.0821
    torr =  62.4
    mm Hg = 62.4
    kPa =   8.31

# r(pressure_type) -> float

"""

R = { #all lowercase
    "atm": 0.0821, #no spaces group
    "torr": 62.4,
    "mmhg": 62.4,
    "kpa": 8.31,

    "mm hg": 62.4, #with spaces

    0: 0.0821,  # atm
    1: 62.4,    # torr / mm Hg
    2: 8.31     # kPa
}

def r(pressure_type):
    r_value = R.get(pressure_type.lower())
    if r_value == None:
        print(f"Error: no pressure type \"{pressure_type}\"")
        quit(1)
    return r_value

def print_R(extra_line=False):
    print("r =\t0.0821\t@ atm,\n\t62.4\t@ torr/mmHg\n\t8.31\t@ kPa")
    if extra_line:
        print()
