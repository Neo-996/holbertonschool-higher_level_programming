#!/usr/bin/python3
"""
Module that defines a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers and returns the result.

    a and b must be integers or floats; otherwise,
    raise a TypeError exception with the message:
    'a must be an integer' or 'b must be an integer'.

    Floats are casted to integers before addition.

    Args:
        a (int or float): first number
        b (int or float): second number (default 98)

    Returns:
        int: sum of a and b as integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
