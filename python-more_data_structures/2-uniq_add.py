#!/usr/bin/python3
"""Module that defines a function to add unique integers in a list."""


def uniq_add(my_list=[]):
    """Add all unique integers in a list, only once for each integer.

    Args:
        my_list (list): The list of integers.

    Returns:
        int: The sum of the unique integers in my_list.
    """
    return sum(set(my_list))
