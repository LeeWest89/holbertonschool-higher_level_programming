#!/usr/bin/python3
"""Unitest for base.py"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Unittest for class Base"""

    def test_expected_id(self):
        Base._Base__nb_objects = 0
        ob = Base(5)
        self.assertEqual(ob.id, 5)

    def test_two_argument_id(self):
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            Base(1, 2)

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
        ob1 = Base(1)
        ob2 = Base(1)
        self.assertNotEqual(ob1, ob2)
        self.assertEqual(ob1.id, ob2.id)

    def test_negative_id(self):
        Base._Base__nb_objects = -10
        ob1 = Base()
        ob2 = Base()
        self.assertEqual(ob1.id, -9)
        self.assertEqual(ob2.id, -8)

    def test_after_unique_id(self):
        Base._Base__nb_objects = 0
        ob1 = Base()
        ob2 = Base(100)
        ob3 = Base()
        self.assertEqual(ob3.id, 2)

    def test_float_id(self):
        Base._Base__nb_objects = 0
        ob1 = Base(0.5)
        ob2 = Base()
        ob3 = Base(1.5)
        self.assertEqual(ob1.id, 0.5)
        self.assertEqual(ob2.id, 1)
        self.assertEqual(ob3.id, 1.5)

    def test_str_id(self):
        Base._Base__nb_objects = 0
        ob1 = Base("hello")
        ob2 = Base()
        self.assertEqual(ob1.id, "hello")
        self.assertEqual(ob2.id, 1)

    def test_list_id(self):
        Base._Base__nb_objects = 0
        ob1 = Base([1, 2, 3])
        ob2 = Base([])
        ob3 = Base()
        self.assertEqual(ob1.id, [1, 2, 3])
        self.assertEqual(ob2.id, [])
        self.assertEqual(ob3.id, 1)

    def test_dict_id(self):
        Base._Base__nb_objects = 0
        ob1 = Base({"a": 1, "b": 2})
        ob2 = Base({})
        ob3 = Base()
        self.assertEqual(ob1.id, {"a": 1, "b": 2})
        self.assertEqual(ob2.id, {})
        self.assertEqual(ob3.id, 1)

    def test_bool_id(self):
        Base._Base__nb_objects = 0
        ob1 = Base(True)
        ob2 = Base()
        self.assertEqual(ob1.id, True)
        self.assertEqual(ob2.id, 1)

    def test_tuple_id(self):
        Base._Base__nb_objects = 0
        ob1 = Base((1, 3))
        ob2 = Base()
        self.assertEqual(ob1.id, (1, 3))
        self.assertEqual(ob2.id, 1)

class TestBase_to_json_string(unittest.TestCase):
    def test_to_json_string(self):
        sample = [{'a': 1, 'b': 2, 'c': 3},
        ]
        self.assertEqual(Base.to_json_string(sample), 
                         '[{"a": 1, "b": 2, "c": 3}]')

    def test_to_json_string_empty(self):
        sample = []
        self.assertEqual(Base.to_json_string(sample),
                         '[]')

    def test_to_json_string_None(self):
        sample = None
        self.assertEqual(Base.to_json_string(sample),
                         '[]')

class TestBase_save_to_file(unittest.TestCase):
    pass

class TestBase_from_json_string(unittest.TestCase):
    pass

class TestBase_create(unittest.TestCase):
    pass

class TestBase_load_json_string(unittest.TestCase):
    pass
