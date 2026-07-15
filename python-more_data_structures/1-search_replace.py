#!/usr/bin/python3
"""Module that defines a function to search and replace in a list."""


def search_replace(my_list, search, replace):
    """Replace all occurrences of an element by another in a new list.

    Args:
        my_list (list): The initial list.
        search: The element to replace in the list.
        replace: The new element.

    Returns:
        list: A new list with all occurrences of search replaced
            by replace.
    """
    return [replace if item == search else item for item in my_list]
