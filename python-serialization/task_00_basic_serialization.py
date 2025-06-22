#!/usr/bin/python3
"""Basic serialization module for Python dict <-> JSON file."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a dictionary and save it to a JSON file.

    Args:
        data (dict): Dictionary to serialize.
        filename (str): Target JSON file name.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize a dictionary from a JSON file.

    Args:
        filename (str): Source JSON file name.

    Returns:
        dict: Deserialized dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
