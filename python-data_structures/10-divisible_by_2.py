#!/usr/bin/python3
"""Defines a function that checks divisibility by 2 for each element."""


def divisible_by_2(my_list=[]):
    """Returns a list of booleans indicating divisibility by 2."""
    result = []
    for num in my_list:
        result.append(num % 2 == 0)
    return result
