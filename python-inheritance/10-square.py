#!/usr/bin/python3
"""New class Square inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Sets up the Square"""
    def __init__(self, size):
        """Calls integer_validator for size"""
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """Using super to call method, returns the area of the square"""
        return (self.__size * self.__size)

    def __str__(self):
        """Function to return info in desired format"""
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
