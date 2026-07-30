#!/usr/bin/python3
"""Module that prints text with indentation after punctuation.

This module defines a single function, text_indentation, that
prints a block of text and adds two new lines after every
occurrence of '.', '?' or ':'.
"""


def text_indentation(text):
    """Print a text with 2 new lines after '.', '?' and ':'.

    Args:
        text (str): the text to print.

    Returns:
        None

    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    stripped_text = text.strip()
    line = ""
    for i, char in enumerate(stripped_text):
        if char == " " and line == "":
            continue
        line += char
        if char in ".?:":
            print(line.strip())
            print()
            line = ""
    if line.strip():
        print(line.strip(), end="")
