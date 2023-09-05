#!/usr/bin/python3

def uppercase(str):

    s = ""

    for char in str:
        if 'a' <= char <= 'z':
            upper = chr(ord(char) - ord('a') + ord('A'))
            s += upper
        else:
            s += char
    print("{1}".format(s))
