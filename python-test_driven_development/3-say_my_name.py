#!/usr/bin/python3
"""Python Task 3. File numbering offset due to formatting error."""


def say_my_name(first_name, last_name=""):
    """Prints 'My name is <first_name> <last_name>'.

    Args:
        first_name (str): First name
        last_name (str): Last name (optional)
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print("My name is " + first_name, end="")
    if first_name != "":
        print(" ", end="")
    print(last_name)
