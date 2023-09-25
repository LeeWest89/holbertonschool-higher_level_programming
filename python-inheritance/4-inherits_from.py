#!/usr/bin/python3
"""Checks if the object is an instance of a class that inherited class"""


def inherits_from(obj, a_class):
    """Check if same type as class inherited from"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    else:
        return (False)
