#!/usr/bin/python3
"""Module that returns a tuple with a string's length and first char."""


def multiple_returns(sentence):
    """Return a tuple: (length of sentence, first character or None)."""
    if len(sentence) == 0:
        first_char = None
    else:
        first_char = sentence[0]
    return (len(sentence), first_char)
