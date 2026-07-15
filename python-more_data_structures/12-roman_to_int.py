#!/usr/bin/python3
"""Module that defines a function to convert a Roman numeral to int."""


def roman_to_int(roman_string):
    """Convert a Roman numeral string to an integer.

    Args:
        roman_string (str): A Roman numeral between 1 and 3999.

    Returns:
        int: The integer value of roman_string, or 0 if
            roman_string is not a string or is None.
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    for i, char in enumerate(roman_string):
        value = values.get(char, 0)
        if i + 1 < len(roman_string) and value < values.get(
                roman_string[i + 1], 0):
            total -= value
        else:
            total += value

    return total
