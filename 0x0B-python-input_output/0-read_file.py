#!/usr/bin/python3
"""Defines a text fille reading function"""


def read_file(filenam=""):
    """Print the contents of a UTF8 text file to stdout"""
    with open(filename, encoding="UTF-8") as f:
        print(f.read(), end="")
