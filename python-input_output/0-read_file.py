#!/usr/bin/python3
"""module provides a function to 
read and print a UTF-8 text file to stdout."""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.

    Args:
        filename (str): The name of 
the file to read. Defaults to an empty string.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
