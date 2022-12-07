#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None or len(matrix) is 0 or matrix[0] is None:
        return matrix
    return [[i ** 2 for i in j] for j in matrix]
