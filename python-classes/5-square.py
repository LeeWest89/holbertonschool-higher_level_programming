#!/usr/bin/python3
"""Defines the class Square."""


class Square:
    """Square with a size."""
    def __init__(self, size=0):
        """Intializes the Square."""
        self.__size = size

    @property
    def size(self):
        """Returns the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Square is set"""
        if type(value) is not int:
            """Checks if vaule is an int"""
            raise TypeError("size must be an integer")
        elif value < 0:
            """Checks if value is positive"""
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the stdout of the square using #"""
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
