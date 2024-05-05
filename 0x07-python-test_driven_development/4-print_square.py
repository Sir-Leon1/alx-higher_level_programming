#!/usr/bin/python3
"""Defines  square-printing function."""


def print_square(size):
    """Print a sqaure with the # character"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
