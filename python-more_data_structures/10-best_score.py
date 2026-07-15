#!/usr/bin/python3
"""Module that defines a function to find the key with the best score."""


def best_score(a_dictionary):
    """Return the key with the biggest integer value.

    Args:
        a_dictionary (dict): A dictionary with integer values.

    Returns:
        The key with the highest value, or None if a_dictionary is
        None or empty.
    """
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
