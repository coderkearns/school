#!/usr/bin/env python3
# chem/units.py

"""Units:

MW = molecular weight

mols = mass / MW
# mol(mass, mw) -> float

T = temp in K
t = temp in C

T = t + 273
t = T - 273
# K(t) -> float
# c(t) -> float

"""


def mol(mass, mw):
    return mass / mw

def kelvins(t):
    return t + 273

def celcius(t):
    return t - 273
