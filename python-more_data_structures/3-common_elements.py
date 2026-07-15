#!/usr/bin/python3
"""Module that defines a function to find common elements of two sets."""


def common_elements(set_1, set_2):
    """Return a set of common elements in two sets.

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: The elements present in both set_1 and set_2.
    """
    return set_1 & set_2
