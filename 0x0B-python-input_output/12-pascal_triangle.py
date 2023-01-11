#!/usr/bin/python3

"""returns a list of pascal triangle
coefficients"""


def pascal_triangle(n):
    """function to return pascal triangle
    coeffecients as list of lists"""

    if n < 1:
        my_list = []
        return my_list
    else:
        list_i = [[1]]
        for i in range(n - 1):
            temp = [0] + list_i[-1] + [0]

            row = []

            for j in range(len(list_i[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            list_i.append(row)
        return list_i
