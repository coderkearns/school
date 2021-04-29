#!/usr/bin/env python3

doc = """
## Hyperbola

`::__init__(name)`
- `name`: the name to use in greetings

`::hi`
- `greeting`: The greeting to use, defaults to "Hello, "
- `punctuation`: A puctuation character, defualts to "!"

`.name`
- The name passed into `__init__`


"""
__doc__ = doc

class Hyperbola():
    __doc__ = doc

    def __init__(self, name):
        self.name = name

    def hi(self, greeting="Hello, ", puctuation="!"):
        return greeting + self.name + puctuation


def main(a, b, c):
    pass

if __name__ == '__main__':
    from util import get_vars
    main(**get_vars({}))
