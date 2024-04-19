#!/usr/bin/python3


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """initialze a new rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """gET/ SET WIDTH OF THE RECTANGLE."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Width must be integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/ set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value
