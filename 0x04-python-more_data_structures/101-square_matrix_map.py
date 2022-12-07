#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda i: list(i), map(lambda x: x * x, matrix[i])))
