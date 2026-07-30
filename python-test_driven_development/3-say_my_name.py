#!/usr/bin/python3
"""Module that prints a person's full name.

This module defines a single function, say_my_name, that prints
a message of the form "My name is <first name> <last name>".
"""


def say_my_name(first_name, last_name=""):
    """Print a message with a person's first and last name.

    Args:
        first_name (str): the person's first name.
        last_name (str): the person's last name, defaults to "".

    Returns:
        None

    Raises:
        TypeError: if first_name is not a string.
        TypeError: if last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
