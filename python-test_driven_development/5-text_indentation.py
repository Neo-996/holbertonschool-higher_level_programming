#!/usr/bin/python3
"""
This module defines the `text_indentation` function, which formats a string
by adding two newlines after each occurrence of `.`, `?`, or `:`.
"""


def text_indentation(text):
    """Function that prints text with 2 new lines after each of these characters: '.', '?', and ':'"""
    
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiters = ".?:"
    temp = ""

    for char in text:
        # Ensure char is a string (char is the individual character in the loop)
        if isinstance(char, str):  
            temp += char
            if char in delimiters:
                print(temp.strip())  # Print and strip the temp string
                print()  # Newline after delimiter
                temp = ""  # Reset temp for next sentence
        else:
            # In case the text contains non-string values like integers, raise an error
            raise TypeError("text must be a string")

    # Handle any remaining text after the loop ends
    if temp:
        print(temp.strip())
