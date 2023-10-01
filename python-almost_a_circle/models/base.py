#!/usr/bin/python3
"""Base class"""


import json


class Base:
    """Base classfor id"""

    __nb_objects = 0

    def __init__(self, id=None):
        """How to find id"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        file = cls.__name__ + ".json"
        with open(file, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_d = [ob.to_dictionary() for ob in list_objs]
                f.write(Base.to_json_string(list_d))
