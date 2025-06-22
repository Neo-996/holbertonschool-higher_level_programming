#!/usr/bin/python3
"""
Script that adds all command line arguments to a Python list,
then saves them to a JSON file 'add_item.json'.
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    # Try to load existing list from the file
    items = load_from_json_file(filename)
except FileNotFoundError:
    # If file doesn't exist, start with an empty list
    items = []

# Append all command line arguments (except the script name)
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
