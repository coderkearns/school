#!/usr/bin/env python3
# classes/name_of_file.py

doc = """
An explanation of the class.
Each part and it's function:

TemplateClass(name)
._name          The inner var to store name
+hi             Says hi
    (greeting, puctuation)
        greeting    optional, defualt "Hello, "
        puctuation  optional, defualt "!"

#use .attribute to show attributes, and +method to show methods.
#methods can be one-line:
+foo(bar)   does foo on bar
#or multiline:
+foo            does foo on bar
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
