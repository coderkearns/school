#!/usr/bin/env python3
# determiants.py

"""Determiant:
A square matrix.
determiant# is a determiant with the dimensions of "# x #"

| a b | = ad - bc
| c d |
# determiant2(a,b,c,d) -> float

| a b c | = aei+bfg+cdb-gec-hfa-idb
| d e f |
| g h i |
# determiant2(a,b,c,d) -> float
"""


def determiant2(a,b,c,d):
    return ((a*d)-(b*c))

def determiant3(a,b,c,d,e,f,g,h,i):
    return ( (a*e*i) + (b*f*g) + (c*d*h) - (g*e*c) - (h*f*a) - (i*d*b) )

if __name__ == "__main__":
    from util import get_vars

    print("|a b c, d e f, g h i| =\naei + bfg + cdb - gec - kfa - idb")
    vars = get_vars({"a":float,"b":float,"c":float,"d":float,"e":float,"f":float,"g":float,"h":float,"i":float,})

    print(determiant3(**vars))
