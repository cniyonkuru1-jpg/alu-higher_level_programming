#!/usr/bin/python3
"""Defines a function that replaces an element in a list."""


def replace_in_list(my_list, idx, element):
    """Replaces an element at a specific index."""
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    my_list[idx] = element
    return my_list
