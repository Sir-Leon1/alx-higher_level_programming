#!/usr/bin/pyhton3

def no_c(my_string):
    """Remove all character c and C from a sring"""
    copy = [x for x in my_string if c != 'c' and x != 'C']
    return ("".join(copy))
