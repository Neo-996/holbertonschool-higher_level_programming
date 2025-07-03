#!/usr/bin/python3
"""Python Task 5. Error in file numbering due to formatting scheme."""


def text_indentation(text):
    """Prints text with two new lines after '.', '?', or ':'.

    Args:
        text (str): The input string to modify.
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
