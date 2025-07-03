#!/usr/bin/python3
"""
Imports the add function from add_0.py, adds two integers, and prints the result
in the format: "<a value> + <b value> = <add(a, b) value>".
Executed only when run directly, not when imported.
"""

from add_0 import add

a = 1
b = 2
print("{} + {} = {}".format(a, b, add(a, b)))
