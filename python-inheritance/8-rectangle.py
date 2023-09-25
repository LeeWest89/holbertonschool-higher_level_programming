#!/usr/bin/python3
"""Class Rectangle inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Sets up class Rectangle"""
    def __init__(self, width, height):
        """Calls integer_validator forheight and width"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
