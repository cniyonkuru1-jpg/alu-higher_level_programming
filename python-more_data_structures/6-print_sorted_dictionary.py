#!/usr/bin/python3
"""Module that defines a function to print a dictionary sorted by key."""


def print_sorted_dictionary(a_dictionary):
    """Print a dictionary by ordered keys.

    Only the keys of the first level are sorted; keys of any nested
    dictionary are left as is.

    Args:
        a_dictionary (dict): The dictionary to print.
    """
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
