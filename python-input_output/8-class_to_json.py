#!/usr/bin/python3
def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dict, string, int, bool) for JSON serialization of an object.
    """
    return obj.__dict__
