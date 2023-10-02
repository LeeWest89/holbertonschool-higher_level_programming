#!/usr/bin/python3
"""Unitest for base.py"""


import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base

class TestSquare(unittest.TestCase):
    """Unittest for Square class"""

    def test_square_no_arguments(self):
        with self.assertRaises(TypeError):
            Square()

    def test_square_is_base(self):
        self.assertIsInstance(Square(2), Base)

    def test_square_is_rectangle(self):
        self.assertIsInstance(Square(2), Rectangle)
