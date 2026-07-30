#!/usr/bin/python3
"""Module for printing a square.

This module provides a function that prints a square using the # character.
"""


def print_square(size):
    """Prints a square with the character #.

    Args:
        size: The side length of the square, must be a non-negative integer.

    Raises:
        TypeError: If size is not an integer, or if it is a float and less
                   than 0.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
