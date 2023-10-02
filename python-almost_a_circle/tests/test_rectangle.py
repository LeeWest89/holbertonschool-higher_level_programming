#!/usr/bin/python3
"""Unitest for base.py"""


import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Unittest for rectangle.py"""

# General Test

    def test_no_argument(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_argument(self):
        with self.assertRaises(TypeError):
            Rectangle(10)

    def test_too_many_argument(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 5, 0, 0, 7, 8, 9, 10)

# Width Test

    def test_width_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 5)

    def test_width_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Hello", 5)

    def test_width_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 5)

    def test_width_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"A": 1, "B": 2}, 5)

    def test_width_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2), 5)

    def test_width_range(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(3), 5)

    def test_width_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(2.5, 5)

    def test_width_floati(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 5)

    def test_width_floatn(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 5)

    def test_width_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 5)

    def test_width_frozenset(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3}), 5)

    def test_width_bool(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 5)

    def test_width_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 5)

    def test_width_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 5)

# Height Test

    def test_height_none(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, None)

    def test_height_str(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, "Hello")

    def test_height_list(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, [1, 2, 3])

    def test_height_dict(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, {"A": 1, "B": 2})

    def test_height_tuple(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, (1, 2))

    def test_height_range(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, range(3))

    def test_height_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, 2.5)

    def test_height_floati(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, float('inf'))

    def test_height_floatn(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, float('nan'))

    def test_height_set(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, {1, 2, 3})

    def test_height_frozenset(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, frozenset({1, 2, 3}))

    def test_height_bool(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, True)

    def test_height_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(5, 0)

    def test_height_negative(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(5, -1)

# X

    def test_x_none(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 5, None)

    def test_x_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 5, "Hello")

    def test_x_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 3, [1, 2, 3])

    def test_x_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 3, {"A": 1, "B": 2})

    def test_x_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 3, (1, 2))

    def test_x_range(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 3, range(3))

    def test_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 3, 2.5)

    def test_x_floati(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 3, float('inf'))

    def test_x_floatn(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 3, float('nan'))

    def test_x_set(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 3, {1, 2, 3})

    def test_x_frozenset(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 3, frozenset({1, 2, 3}))

    def test_x_bool(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 3, True)

    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 5, -1)

# Y

    def test_y_none(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 5, 0, None)

    def test_y_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 5, 0, "Hello")

    def test_y_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 3, 0, [1, 2, 3])

    def test_y_dict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 3, 0, {"A": 1, "B": 2})

    def test_y_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 3, 0, (1, 2))

    def test_y_range(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 3, 0, range(3))

    def test_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 3, 0, 2.5)

    def test_y_floati(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 3, 0, float('inf'))

    def test_y_floatn(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 3, 0, float('nan'))

    def test_y_set(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 3, 0, {1, 2, 3})

    def test_y_frozenset(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 3, 0, frozenset({1, 2, 3}))

    def test_y_bool(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 3, 0, True)

    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 5, 0, -1)
