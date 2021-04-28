#!/usr/bin/env python3
# util.py

"""
#get_vars({name: type}) -> {}
get_vars takes a dict of vars and their types, then returns the user input. Note: type can be any function that takes a string, not just int, float, or some other type. (or class?)
EX: get_vars({"a": int, "b": int}) -> {"a": 1, "b": 3}

#alias(old_dict: {}, aliases: {}) -> {}
alias takes a dict (usualy obtained from get_vars), and aliases each to the name as given in the the aliases input.
Ex: mydict = {"a": 1, "b": 3}
alias({"a": "numberone", "b": "numbertwo"}, mydict) -> {"numberone": 1, "numbertwo": 3}

#strip_float(flt: float) -> [ int or float ]
check if the float does not have decimals. If so, turns it into an int. If it has decimals, it just returns the input.
EX: strip_float(4.00) -> int(4)
EX: strip_float(9.273) -> float(9.273)

#strip_all(iterable) -> list[ [int or float] ]
Runs strip_float on each item in the iterable.
EX: strip_all(3.0,7,9.00) -> (3, 7, 9)

#new_error(name) -> class (extending Exception)
Creates a new Exception class
EX: NameException = new_error("NameException")
"""

def get_vars(var_dict):
    vars = {}
    for var, vartype in var_dict.items():
        vars = {**vars, **{var:
            vartype(input(f"{var}=? "))
        }}
    return vars


def alias(old_dict, aliases):
    new_dict = {}
    for k, v in aliases.items():
        new_dict[v] = old_dict[k]
    return new_dict

def strip_float(flt):
    flt = float(flt) # make sure it is a float
    hasdecimal = str(flt).split(".")[1] != "0"
    if not hasdecimal: return int(flt)
    return flt

def strip_all(*args, iter=False):
    if iter:
        return map(strip_float, iter)
    return map(strip_float, args)

def newerror(name):
    return type(name, (Exception, object), {})
