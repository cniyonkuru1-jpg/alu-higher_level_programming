#!/usr/bin/python3
"""Module that defines a function to square every value in a matrix."""


def square_matrix_simple(matrix=[]):
    """Compute the square of every integer in a 2D matrix.

    Args:
        matrix (list): A 2 dimensional list of integers.

    Returns:
        list: A new matrix, same size as matrix, where each value
            is the square of the corresponding value in matrix.
    """
    return [[value ** 2 for value in row] for row in matrix]
