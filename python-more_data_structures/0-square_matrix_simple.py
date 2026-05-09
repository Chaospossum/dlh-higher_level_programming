#!/usr/bin/python3
"""Module for square_matrix_simple method."""


def square_matrix_simple(matrix=[]):
    """Computes the square of all integers in a matrix."""
    return [list(map(lambda x: x ** 2, row)) for row in matrix]
