#!/usr/bin/env python3
# perfect_roots.py

from json import dumps as dump_json
from yaml import full_load as load_yaml

with open("config.yaml", "r") as cfg_file:
    cfg = load_yaml(cfg_file)

# Creates a list to iterate over for roots and numbers:
# EX: [2, 3, 4]
roots_list = list(range(2, cfg["numbers"]["number_of_roots"]+1))
# EX: [1,2,3, ...1000]
perfect_numbers_list = list(range(1, cfg["numbers"]["perfect_numbers_per_root"]+1))


data = {}

for root in roots_list:
    data[root] = {}
    for number in perfect_numbers_list:
        perfect_exponent = number**root
        data[root][perfect_exponent] = {
        "number":number,
        "exponent":root,
        "ans":perfect_exponent
        }

# convert data to json and place in output file
data = dump_json(data, indent=cfg["output"]["indent"])
with open(cfg["output"]["file"], "w+") as file:
    file.write(data+"\n")
