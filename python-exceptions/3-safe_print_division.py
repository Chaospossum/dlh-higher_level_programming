#!/usr/bin/python3
"""Module for safe_print_division method."""


def safe_print_division(a, b):
    """Divides two integers and prints the result."""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
    return result
