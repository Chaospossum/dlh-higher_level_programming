#!/usr/bin/python3
"""Returns a copy of a list with one element replaced."""


def new_in_list(my_list, idx, element):
    """Replace an element in a list at a specific position.

    The original list is not modified. If the index is negative or
    out of range, returns a copy of the original list unchanged.

    Args:
        my_list: The original list.
        idx: The index at which to replace the element.
        element: The new element to place at idx.

    Returns:
        A new list with the element replaced (or an unchanged copy).
    """
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    new_list = my_list[:]
    new_list[idx] = element
    return new_list
