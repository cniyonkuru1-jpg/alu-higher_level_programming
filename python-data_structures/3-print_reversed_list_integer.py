#!/usr/bin/python3
"""Defines a function that prints a list of integers in reverse."""


def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list, one per line, in reverse order."""
    i = len(my_list) - 1
    while i >= 0:
        print("{:d}".format(my_list[i]))
        i -= 1
