#!/usr/bin/python3
"""Finds the biggest integer in a list."""


def max_integer(my_list=[]):
    """Return the biggest integer in a list, or None if empty.

    Args:
        my_list: A list of integers (default empty list).

    Returns:
        The biggest integer, or None if the list is empty.
    """
    if not my_list:
        return None
    biggest = my_list[0]
    for num in my_list[1:]:
        if num > biggest:
            biggest = num
    return biggest
