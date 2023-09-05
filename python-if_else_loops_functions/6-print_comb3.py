#!/usr/bin/python3

for n1 in range(10):
    for n2 in range(n1 + 1, 10):
        if n1 < 8:
            print("{:d}{:d}, ".format(n1, n2), end="")
        else:
            print("{:d}{:d}".format(n1, n2))
