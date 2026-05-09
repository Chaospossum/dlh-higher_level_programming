#!/usr/bin/python3
"""Finds which integers in a list are divisible by 2."""


def divisible_by_2(my_list=[]):
    """Return a list of booleans for divisibility by 2.

    Each position in the output list is True if the integer at the
    same position in the input is divisible by 2, False otherwise.

    Args:
        my_list: A list of integers (default empty list).

    Returns:
        A list of booleans, same length as my_list.
    """
    return [num % 2 == 0 for num in my_list]
