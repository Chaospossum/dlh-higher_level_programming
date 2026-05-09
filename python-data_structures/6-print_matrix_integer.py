#!/usr/bin/python3
"""Prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers, rows separated by newlines.

    Args:
        matrix: A list of lists of integers (default [[]]).
    """
    for row in matrix:
        print(" ".join("{:d}".format(num) for num in row))
