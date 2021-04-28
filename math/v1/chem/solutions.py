#!/usr/bin/env python3
# chem/solutions.py

"""Solutions and Concentrations:

MW = molecular weight
mols = mass / MW

mass percent = ( mass of solute / total mass ) * 100
# mass_percent(mass, total_mass) -> float

mole fraction = ( moles solute / total moles )
# mole_fraction(mol, total_mol) -> float

molality = ( moles solute / kg solovent )
# molality(mol, kg) -> float

molarity = ( moles solute / liters solution )
# molarity(mol, v) -> float

"""

def mass_percent(mass, total_mass):
    return ( mass / total_mass ) * 100

def mole_fraction(mol, total_mol):
    return mol / total_mol

def molality(mol, kg):
    return mol / kg

def molarity(mol, v):
    return mol / v
