#!/usr/bin/python3
"""Defines a function that divides all elements of a matrix."""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.
    
    Args:
        matrix (list of lists): matrix of integers/floats.
        div (int/float): divisor.

    Returns:
        New matrix with all elements divided by div, rounded to 2 decimals.

    Raises:
        TypeError: if matrix or div is of incorrect type.
        ZeroDivisionError: if div is zero.
        ValueError: if div is NaN or Infinity.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len({len(row) for row in matrix}) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if div != div:
        raise ValueError("cannot convert float NaN to integer")
    if div == float('inf') or div == float('-inf'):
        raise OverflowError("cannot convert float infinity to integer")

    return [[round(num / div, 2) for num in row] for row in matrix]
