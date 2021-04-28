#!/usr/bin/env python3
# classes/name_of_file.py

doc = """
## Circle:

(x-h)^2 + (y-k)^2 = r^2

Where center = Point(h, k)

"""
__doc__ = doc

import matplotlib.pyplot as plt
import math
from .point import Point


class Circle():
    __doc__ = doc

    def __init__(self, h, k, r):
        self.center = Point(h, k)
        self.radius = r

    def __repr__(self):
        return self.equation

    def json(self):
        return f"({self.center.json()}, {self.radius})"

    def graph(self):
        c = plt.Circle((self.center.x, self.center.y), self.radius, fill=False)

        ax = plt.gca()
        ax.cla()
        ax.set_aspect('equal', adjustable='box')
        ax.set_xlim((
            self.center.x-self.radius*1.5,
            self.center.x+self.radius*1.5
        ))
        ax.set_ylim((
            self.center.y-self.radius*1.5,
            self.center.y+self.radius*1.5
        ))

        ax.add_patch(c)
        ax.plot(self.center.x,self.center.y, marker="o", color="black")

        ax.plot(0, 0, marker="+", color="black")

        plt.show()
        return ax

    @property
    def equation(self):
        return f"(x - {self.center.x})^2 + (y - {self.center.y})^2 = {self.radius}^2"

    @property
    def area(self):
        return f"π{self.radius**2}"
        #return math.PI * ( self.radius ** 2 )

    @property
    def circumference(self):
        return f"π{self.radius*2}"
        return math.PI*2*self.radius
