#!/usr/bin/python3
def read_file(filename=""):
    """Reads a text file (UTF-8) and prints its contents to stdout.

    Args:
        filename (str): The path to the file to be read.
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')
