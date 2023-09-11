#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    ms = []
    for row in matrix:
        ms.append(list(map(lambda x: x*x, row)))
    return (ms)
