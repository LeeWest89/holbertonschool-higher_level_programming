#!/usr/bin/python3
""" 2-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    try:
        Rectangle()
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.width = -10
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.x = {}
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        Rectangle(1, 2, 3, 1, 3, 4)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
