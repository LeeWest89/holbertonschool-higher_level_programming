#!/usr/bin/python3
"""Defines the class Square."""


class Square:
    """Square with a size."""
    def __init__(self, size=0, position=(0, 0)):
        """Intializes the Square."""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Returns the position in the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets the position"""
        if type(value[0], value[1]) is not int:
            """Checks if value is tuple of two postive int"""
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value) is not tuple:
            """Checks if value is tuple of two postive int"""
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            """Check if position has two elements"""
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value(value[0] < 0 or value[1] < 0):
            """Checks if value isless than zero"""
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__postion = value

    def area(self):
        """Returns the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the stdout of the square using # and spaces"""
        if self.__size == 0:
            print()
            return ()
        for k in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
