#!/usr/bin/python3
"""Module for text indentation.

This module provides a function that prints text with 2 new lines after
each of these characters: '.', '?', and ':'.
"""


def text_indentation(text):
    """Prints text with 2 new lines after '.', '?', and ':'.

    Args:
        text: The input text, must be a string.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    prev = 0
    for i, c in enumerate(text):
        if c in ".?:":
            line = text[prev:i + 1].strip()
            if line:
                print(line)
            print()
            prev = i + 1
    last = text[prev:].strip()
    if last:
        print(last, end="")
