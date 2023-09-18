#!/usr/bin/python3
"""
Function tht adds two numbers together and returns an integer
"""
def add_integer(a, b=98):


    """Adds to Integers together"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a + b)
