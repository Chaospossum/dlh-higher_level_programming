#!/usr/bin/python3
"""Prints a list of integers in reverse order."""


def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order, one per line.

    Args:
        my_list: List of integers (default empty list).
    """
    for i in my_list[::-1]:
        print("{:d}".format(i))
