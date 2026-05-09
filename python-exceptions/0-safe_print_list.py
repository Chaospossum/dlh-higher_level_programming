#!/usr/bin/python3
"""Module for safe_print_list method."""


def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list and returns the count printed."""
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            break
    print()
    return count
