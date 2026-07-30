#!/usr/bin/python3
"""Module that prints a square using the # character.

This module defines a single function, print_square, that prints
a square of a given size made entirely of '#' characters.
"""


def print_square(size):
    """Print a square with the character #.

    Args:
        size (int): the length of each side of the square.

    Returns:
        None

    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is a negative integer.
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
