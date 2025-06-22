#!/usr/bin/python3
"""
This module defines a function that writes text to a file
and returns character count.
"""


def write_file(filename="", text=""):
    """Write text to a file and return number of characters written."""
    with open(filename, "w", encoding="utf-8") as f:
         return f.write(text)
