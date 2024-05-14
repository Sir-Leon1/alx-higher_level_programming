#!/usr/bin/python3
"""Defines a rectangle subclass square."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Initialize a new square."""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
