#!/usr/bin/python3
"""Adds two tuples element-wise on the first two elements."""


def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples and return a new tuple of two integers.

    Missing elements are treated as 0. Only the first two elements
    of each tuple are considered.

    Args:
        tuple_a: The first tuple (default empty).
        tuple_b: The second tuple (default empty).

    Returns:
        A tuple of two integers (sum of first elements, sum of second).
    """
    a0 = tuple_a[0] if len(tuple_a) >= 1 else 0
    a1 = tuple_a[1] if len(tuple_a) >= 2 else 0
    b0 = tuple_b[0] if len(tuple_b) >= 1 else 0
    b1 = tuple_b[1] if len(tuple_b) >= 2 else 0
    return (a0 + b0, a1 + b1)
