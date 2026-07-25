#!/usr/bin/python3
"""Defines a list subclass that can print itself sorted."""


class MyList(list):
    """Represent a list that can also display its elements sorted."""

    def print_sorted(self):
        """Print all the integers of the list in ascending order."""
        print(sorted(self))
