#!/usr/bin/python3
"""Defines a function that deletes an item at a specific index."""


def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list."""
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    return my_list[:idx] + my_list[idx + 1:]
