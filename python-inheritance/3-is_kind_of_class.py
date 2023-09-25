#!/usr/bin/python3
"""Function that checks if object is the same class as what it inherits"""


def is_kind_of_class(obj, a_class):
    """Check if same type as class inherited from"""
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
