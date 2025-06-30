#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): A matrix of integers/floats.
        div (int/float): The number to divide by.

    Returns:
        list: New matrix with each element divided by div.

    Raises:
        TypeError: If matrix isn't a list of lists of numbers,
                   if rows are not the same size,
                   or if div isn't a number.
        ZeroDivisionError: If div is 0.
        ValueError/OverflowError: If div is NaN or inf.
    """
    if not isinstance(matrix, list) or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if not all(
        isinstance(x, (int, float)) for row in matrix for x in row
    ):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    row_lengths = list(map(len, matrix))
    if row_lengths.count(row_lengths[0]) != len(row_lengths):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if div != div:
        raise ValueError("cannot convert float NaN to integer")
    if div == float("inf") or div == float("-inf"):
        raise OverflowError("cannot convert float infinity to integer")

    return [[round(x / div, 2) for x in row] for row in matrix]
