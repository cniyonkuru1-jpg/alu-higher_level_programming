#!/usr/bin/python3
"""Module that divides all elements of a matrix.

This module defines a single function, matrix_divided, that returns
a new matrix with every element divided by a given number, rounded
to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a number.

    Args:
        matrix (list of lists of int/float): the matrix to divide.
        div (int or float): the number to divide each element by.

    Returns:
        list of lists of float: a new matrix with every element
        divided by div and rounded to 2 decimal places.

    Raises:
        TypeError: if matrix is not a list of lists of int/float.
        TypeError: if rows of matrix don't all have the same size.
        TypeError: if div is not an int or a float.
        ZeroDivisionError: if div is equal to 0.
    """
    err_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    err_size = "Each row of the matrix must have the same size"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(err_matrix)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(err_matrix)
        for element in row:
            if not isinstance(element, (int, float)) or \
                    isinstance(element, bool):
                raise TypeError(err_matrix)

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError(err_size)

    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
