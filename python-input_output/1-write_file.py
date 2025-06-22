#!/usr/bin/python3
"""This module provides a function to write a string to a UTF-8 text file."""

write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to. Creates the file if it doesn't exist.
        text (str): The string to write to the file.

    Returns:
        int: Number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
