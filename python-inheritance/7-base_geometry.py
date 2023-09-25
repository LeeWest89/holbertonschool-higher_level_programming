#!/usr/bin/python3
"""Creates class BaseGeometry"""


class BaseGeometry:
    """Creates class BaseGeometry"""
    def area(self):
        """Public method that raises Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
