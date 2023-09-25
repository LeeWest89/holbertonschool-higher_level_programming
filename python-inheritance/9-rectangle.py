#!/usr/bin/python3
"""Class Rectangle inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Sets up class Rectangle"""
    def __init__(self, width, height):
        """Calls integer_validator for height and width"""
        super().__init__()
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Using super to call method, returns the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Function to return info in desired format"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
