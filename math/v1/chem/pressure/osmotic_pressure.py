#!/usr/bin/env python3
# chem/osmotic_pressure.py

"""Osmotic Pressure:

Π = osmotic pressure

Π = MRT
Π = M*r*t

M = molarity (M): (mol / volume)
t = Kelvins temp (T)
r = R constant

mass, weight, volume, temp (in C)

# osmotic_pressure(m, w, v, t, pressure_unit) -> float

"""

from .r import r, print_R
from ..solutions import molarity
from ..units import mol, kelvins

def osmotic_pressure(m, w, v, t, pressure_unit):
    return (
        kelvins(t) # T
        * r(pressure_unit) # R
        * molarity( # M:
            mol(m, w), # mols
            v          # liters
        )
    )

if __name__ == "__main__":
    from util import get_vars, alias

    print("Π = MRT")
    print("Π = ((mass/mw)/v)RT")
    print_R()
    print("")

    vars = get_vars({
        "mass":float,
        "mw":float,
        "volume":float,
        "temp (C)":float,
        "pressure type":str
    })

    print(osmotic_pressure(
        **alias(vars, {
            "mass":"m",
            "mw":"w",
            "volume": "v",
            "temp (C)": "t",
            "pressure type": "pressure_unit"
        })
    ))
