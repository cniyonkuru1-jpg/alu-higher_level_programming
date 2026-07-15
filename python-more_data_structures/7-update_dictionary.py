#!/usr/bin/python3
"""Module that defines a function to update a dictionary in place."""


def update_dictionary(a_dictionary, key, value):
    """Replace or add a key/value pair in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to update.
        key (str): The key to add or update.
        value: The value to associate with key.

    Returns:
        dict: The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
