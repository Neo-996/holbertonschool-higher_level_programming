#!/usr/bin/python3
"""
Module to add two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats casted to integers.
    Raises TypeError if a or b is not int or float.
    Returns the sum as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
