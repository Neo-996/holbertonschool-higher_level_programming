#!/usr/bin/python3
"""Module to add two integers and print the result in a formatted string
"""

from add_0 import add  # Importing add() function only once

def main():
    a = 1  # Define a
    b = 2  # Define b
    print(f"{a} + {b} = {add(a, b)}")  # Using one print statement with string format

if __name__ == "__main__":
    main()  # This ensures the code runs only when executed directly
