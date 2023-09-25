#!/usr/bin/python3
"""Function that reads text and prints it to standard input"""


def read_file(filename=""):
    """the function that reads and prints"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
