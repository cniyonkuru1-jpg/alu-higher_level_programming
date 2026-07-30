#!/usr/bin/python3
"""Module that adds two integers.

This module defines a single function, add_integer, that adds
two numbers together after casting them to integers if needed.
"""


def add_integer(a, b=98):
    """Add two integers or floats and return the result as an integer.

    Args:
        a (int or float): the first number to add.
        b (int or float): the second number to add, defaults to 98.

    Returns:
        int: the sum of a and b, with each value cast to int first.

    Raises:
        TypeError: if a is not an integer or float.
        TypeError: if b is not an integer or float.
    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
