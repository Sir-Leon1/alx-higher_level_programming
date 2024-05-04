#!/usr/bin/pyhon3
"""Defones an integer addition function"""


def add_integer(a, b=98):
    """Return the integer addition of a and b

    Float numbers are typecasted to ints b4 addition
    """
    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return (int(a) + int(b)) 
