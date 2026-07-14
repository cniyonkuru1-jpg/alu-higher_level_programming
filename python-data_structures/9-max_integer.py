#!/usr/bin/python3
"""Defines a function that finds the biggest integer in a list."""


def max_integer(my_list=[]):
    """Returns the largest integer in a list, or None if empty."""
    if len(my_list) == 0:
        return None
    biggest = my_list[0]
    for num in my_list:
        if num > biggest:
            biggest = num
    return biggest
