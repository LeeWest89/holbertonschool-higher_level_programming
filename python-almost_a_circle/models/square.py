#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Creates the square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Creates square instance"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        self.height = value
        self.width = value

    def __str__(self):
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Will change attributes to new values"""
        if args:
            att = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, att[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
