#!/usr/bin/python3
"""Defines a class MYIt that inherits from int."""

class MyInt(int):
    """invert int operators == and !="""

    def __eq__(self, value):
        """Override == operator with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """override != operator with == behaviour."""
        return self.real == value
