#!/usr/bin/python3
"""Removes all occurrences of 'c' and 'C' from a string."""


def no_c(my_string):
    """Return a copy of my_string with all 'c' and 'C' removed.

    Args:
        my_string: The input string.

    Returns:
        A new string with no 'c' or 'C' characters.
    """
    result = ""
    for char in my_string:
        if char not in "cC":
            result = result + char
    return result
