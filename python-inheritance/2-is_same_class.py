#!/usr/bin/python3
"""Function that returns True if the object is the class ; otherwise False"""


def is_same_class(obj, a_class):
    """Checks if the obj is the exact type of a_class"""
    return type(obj) is a_class
