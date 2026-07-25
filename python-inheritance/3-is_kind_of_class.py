#!/usr/bin/python3
"""Defines a function that checks class membership, direct or inherited."""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of a_class or one of its subclasses.

    Args:
        obj: The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or a subclass of it.
    """
    return isinstance(obj, a_class)
