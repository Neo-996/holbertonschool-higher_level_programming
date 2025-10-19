#!/usr/bin/python3
"""
This module defines a function that prints text with two new lines after
each '.', '?' or ':' character.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after '.', '?', or ':' characters.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = []
    current = ""

    for c in text:
        current += c
        if c in ".:?":
            result.append(current.strip())
            current = ""

    if current.strip():
        result.append(current.strip())

    for i in range(len(result)):
        print(result[i], end="")
        if i < len(result) - 1:
            print("\n")
