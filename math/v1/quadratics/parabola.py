#!/usr/bin/env python3
# classes/name_of_file.py

doc = """
Parabola is a class to store parabolas. The defualt constructor uses standard form, but you can also use the classmethod   `from_vertex_form`

Parabola(a, b, c)
.abc          The inner var to store name
+hi             Says hi
    (greeting, puctuation)
        greeting    optional, defualt "Hello, "
        puctuation  optional, defualt "!"

#use .attribute to show attributes, and +method to show methods.
#methods can be one-line:
+foo(bar)   does foo on bar
#or multiline:
+foo            does foo pwdon bar
    (bar)
        bar     bar!
"""
__doc__ = doc

class Template():
    __doc__ = doc

    def __init__(self, name):
        self._name = name

    def hi(self, greeting="Hello, ", puctuation="!"):
        return greeting + self._name + puctuation
