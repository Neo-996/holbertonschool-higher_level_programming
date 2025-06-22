#!/usr/bin/python3
"""Module to append a string to a UTF-8 text file."""


def append_write(filename="", text=""):
    """Append text to a file and return the number of characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        # Append text and return number of characters added
        return f.write(text)
