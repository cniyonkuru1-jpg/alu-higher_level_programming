#!/usr/bin/python3
"""Defines a function that replaces an element in a copy of a list."""


def new_in_list(my_list, idx, element):
    """Returns a new list with an element replaced.

    Does not modify the original list.
    """
    new_list = my_list[:]
    if idx < 0 or idx > len(new_list) - 1:
        return new_list
    new_list[idx] = element
    return new_list
