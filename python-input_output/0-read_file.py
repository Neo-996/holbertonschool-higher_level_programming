#!/usr/bin/python3
"""
This module defines a function that reads a text file
and prints its content to stdout.
"""


def read_file(filename=""):
    """read_file function that's read a file and print it"""

    with open(filename, encoding="UTF-8") as f:
        print(f.read(), end="")
