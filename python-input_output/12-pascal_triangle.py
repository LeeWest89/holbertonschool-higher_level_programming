#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """returns a list of integers representing the Pascal's triangle"""
    if n <= 0:
        return ([])

    triangle = [[1]]
    for i in range(1, n):
        l = [1]
        for j in range(1, i):
            l.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        l.append(1)
        triangle.append(l)
    return (triangle)
