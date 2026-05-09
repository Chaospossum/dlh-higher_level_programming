#!/usr/bin/python3
"""Deletes the item at a specific position in a list."""


def delete_at(my_list=[], idx=0):
    """Delete the item at index idx in my_list.

    If idx is negative or out of range, the list is unchanged.

    Args:
        my_list: The list to modify.
        idx: The index of the element to delete.

    Returns:
        The modified list (or the unchanged list if idx is invalid).
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
