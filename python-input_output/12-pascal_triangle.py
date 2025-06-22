#!/usr/bin/python3
"""
Defines a function to generate Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascals triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1]  # First element

        # Fill in the middle elements
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)  # Last element
        triangle.append(row)

    return triang
