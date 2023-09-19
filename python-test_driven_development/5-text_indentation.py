#!/usr/bin/python3
"""Function that prints 2 new lines after . ? :"""


def text_indentation(text):
    """Prints text and 2 new lines after . ? :"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    symbol = ['.', '?', ":"]
    line = []
    c = ""

    for i in text:
        c += i
        if i in symbol:
            line.append(c.strip())
            line.append("\n\n")
            c = ""
    if c:
        line.append(c.strip())
    for a in line:
        print(a, end="")
