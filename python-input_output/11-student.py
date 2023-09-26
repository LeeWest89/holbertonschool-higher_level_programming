#!/usr/bin/python3
"""defines class Student"""


class Student:
    """Defines student info"""
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return (self.__dict__)
        else:
            d = {}
            for i in attrs:
                if hasattr(self, i):
                    d[i] = getattr(self, i)
            return (d)

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
