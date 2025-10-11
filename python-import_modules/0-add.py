#!/usr/bin/python3
"""Module to add two integers and print the result in a formatted string
"""

from add_0 import add  # Importing add() function only once

def main():
    a = 1  # Define a
    b = 2  # Define b
    if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, add(a, b)))
    
