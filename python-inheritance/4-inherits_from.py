#!/usr/bin/python3
"""Defines a function that checks for strict subclass inheritance."""


def inherits_from(obj, a_class):
    """Check if obj's class inherited a_class, without being a_class.

    Args:
        obj: The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class,
            but not an instance of a_class itself.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
