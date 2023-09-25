#!/usr/bin/python3
"""New class Square inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """Sets up the Square"""
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def __str__(self):
        """Function to return info in desired format"""
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
