#!/usr/bin/env python3
# print_ans.py

from json import load as load_json
from yaml import full_load as load_yaml

with open("config.yaml", "r") as cfg_file:
    cfg = load_yaml(cfg_file)

data_file = cfg["output"]["file"]
with open(data_file, "r") as data_file:
    data = load_json(data_file)

def print_exponents():
    for exponent in data.keys():
        for number, num_data in data[exponent].items():
            base = num_data["number"]
            print(f"{base}^{exponent}:\t{number}")
        print()

def print_roots():
    for exponent in data.keys():
        for number, num_data in data[exponent].items():
            base = num_data["number"]
            print(f"{exponent}√ {number}=\t{base}")
        print()

if cfg["print"] == "exponents":
    print_exponents()
elif cfg["print"] == "roots":
    print_roots()
else:
    print("\"{}\" is not a vaild function.\nChoose \"exponents\" or \"roots\".".format(cfg["print"]))
