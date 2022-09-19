#!/usr/bin/python3
"""This module divides integer"""


def matrix_divided(matrix, div):
    """This matrix divides the integers by a given

        Args:
            matrix: matrix to be divivded.
            div: divisoors
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    max = len(matrix[0])
    for r in matrix:
        if any(type(n) not in [int, float] for n in r):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        if max != len(r):
            raise TypeError("Each row of the matrix must have the same size")

    new_mat = []
    for r in matrix:
        row = [round(num / div, 2) for num in r]
        new_mat.append(row)

    return new_mat
