#!/usr/bin/python3
"""Defines a function that returns the length and first character of a string."""


def multiple_returns(sentence):
    """Returns a tuple: (length of sentence, first character or None)."""
    if len(sentence) == 0:
        first_char = None
    else:
        first_char = sentence[0]
    return (len(sentence), first_char)
