#!/usr/bin/python3
"""Unitest for base.py"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unittest for class Base"""

    def test_expected_id(self):
        Base._Base__nb_objects = 0
        ob = Base(id=5)
        self.assertEqual(ob.id, 5)

    def test_no_id(self):
        Base._Base__nb_objects = 0
        ob1 = Base()
        ob2 = Base()
        self.assertEqual(ob1.id, 1)
        self.assertEqual(ob2.id, 2)

    def test_increment(self):
        Base._Base__nb_objects = 0
        ob1 = Base()
        ob2 = Base()
        ob3 = Base()
        ob4 = Base()
        self.assertEqual(Base._Base__nb_objects, 4)

    def test_none(self):
        Base._Base__nb_objects = 0
        ob1 = Base()
        ob2 = Base(None)
        ob3 = Base()
        ob4 = Base(None)
        self.assertEqual(ob1.id, 1)
        self.assertEqual(ob2.id, 2)
        self.assertEqual(ob3.id, 3)
        self.assertEqual(ob4.id, 4)

    def test_same_id(self):
        Base._Base__nb_objects = 0
        ob1 = Base(id=1)
        ob2 = Base(id=1)
        self.assertNotEqual(ob1, ob2)
        self.assertEqual(ob1.id, ob2.id)
