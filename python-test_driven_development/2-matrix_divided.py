#!/usr/bin/python3
"""Module for dividing a matrix.

This module provides a function that divides all elements of a matrix by a
given divisor.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div.

    Args:
        matrix: A list of lists of integers or floats.
        div: The divisor, must be an integer or float.

    Returns:
        list: A new matrix with all elements divided by div, rounded to 2
        decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats, or if
                   rows have different sizes, or if div is not a number.
        ZeroDivisionError: If div is 0.
    """
    if not isinstance(matrix, list) or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if not matrix or not all(len(row) > 0 for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of "
                    "integers/floats"
                )
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(elem / div, 2) for elem in row] for row in matrix]
