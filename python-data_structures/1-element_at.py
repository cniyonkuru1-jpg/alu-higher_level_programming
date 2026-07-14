#!/usr/bin/python3
"""Defines a function that retrieves an element from a list."""


def element_at(my_list, idx):
    """Retrieves an element at a specific index, C-style."""
    if idx < 0 or idx > len(my_list) - 1:
        return None
    return my_list[idx]
