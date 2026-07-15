#!/usr/bin/python3
"""Module that defines a function to find elements unique to each set."""


def only_diff_elements(set_1, set_2):
    """Return a set of all elements present in only one of two sets.

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: The elements present in exactly one of set_1 or set_2.
    """
    return set_1 ^ set_2
