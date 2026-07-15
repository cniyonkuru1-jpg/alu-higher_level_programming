#!/usr/bin/python3
"""Module that defines a function to multiply a list's values."""


def multiply_list_map(my_list=[], number=0):
    """Return a new list with each value multiplied by number.

    Args:
        my_list (list): The list of numbers.
        number: The number to multiply each value by.

    Returns:
        list: A new list, same length as my_list, with each value
            multiplied by number.
    """
    return list(map(lambda n: n * number, my_list))
