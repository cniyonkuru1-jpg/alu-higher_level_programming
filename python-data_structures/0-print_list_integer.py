#!/usr/bin/python3
"""Defines a function that prints all integers of a list."""


def print_list_integer(my_list=[]):
    """Prints all integers of a list, one per line."""
    for i in my_list:
        print("{:d}".format(i))
