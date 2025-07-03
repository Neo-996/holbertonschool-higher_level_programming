#!/usr/bin/python3
"""
This module defines the `text_indentation` function, which formats a string
by adding two newlines after each occurrence of `.`, `?`, or `:`.
"""


def text_indentation(text):
    """
    Prints text with two newlines after each occurrence of '.', '?', or ':'.

    Args:
        text (str): The input string to modify.

    Raises:
        TypeError: If `text` is not a string.
    """
    if type(text) is not str:
        raise TypeError('text must be a string')

    j = 0
    delims = '.?:'

    for i, char in enumerate(text):
        for delim in delims:
            if char is delim:
                j += 1
                text = text[:i + j] + ' ' + text[i + j:]

    words = text.split()

    for word in words:
        if word[-1:] in ".?:":
            print(word, end="\n\n")
        elif word is words[-1]:
            print(word, end="")
        else:
            print(word, end=" ")
