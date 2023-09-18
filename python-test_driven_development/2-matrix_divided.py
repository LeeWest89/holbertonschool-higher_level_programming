#!/usr/bin/python3
"""Divides all elements in a matrix as lon as they are a float or an integer"""


def matrix_divided(matrix, div):
    """Divides all elements in the matrix"""
    nm = []
    result = []
    col = len(matrix[0])

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if len(row) != col:
            raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        for elem in row:
            if type(elem) != int and float:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
    return [list(round(elem/div, 2) for elem in row) for row in matrix]
