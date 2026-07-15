#!/usr/bin/python3
"""Module that defines a function to double all values of a dictionary."""


def multiply_by_2(a_dictionary):
    """Return a new dictionary with all values multiplied by 2.

    Args:
        a_dictionary (dict): A dictionary with integer values.

    Returns:
        dict: A new dictionary with every value doubled.
    """
    return {key: value * 2 for key, value in a_dictionary.items()}
