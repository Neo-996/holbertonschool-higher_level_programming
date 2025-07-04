#!/usr/bin/python3
"""
This module defines a function that prints a square with '#' characters.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer or is a negative float.
        ValueError: If size is less than 0.
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for row in range(size):
        for col in range(size):
            print('#', end="")
        print()
