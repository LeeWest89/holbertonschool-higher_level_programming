#!/usr/bin/python3
"""Defines the class Square."""


class Square:
    """Square with a size."""
    def __init__(self, size=0):
        """Intializes the Square."""
        if type(size) is not int:
            """Checks if size is an int"""
            raise TypeError("size must be an integer")
        elif size < 0:
            """Checks if value of size is a positive"""
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return (self.__size ** 2)
