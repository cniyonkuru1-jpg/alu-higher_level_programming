#!/usr/bin/python3
"""Module that defines a function to delete a key from a dictionary."""


def simple_delete(a_dictionary, key=""):
    """Delete a key from a dictionary.

    If the key doesn't exist, the dictionary is left unchanged.

    Args:
        a_dictionary (dict): The dictionary to update.
        key (str): The key to delete.

    Returns:
        dict: The updated dictionary.
    """
    a_dictionary.pop(key, None)
    return a_dictionary
