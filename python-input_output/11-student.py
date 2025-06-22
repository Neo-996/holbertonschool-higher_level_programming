#!/usr/bin/python3
"""
Module defining the Student class with JSON serialization and deserialization.
"""

class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes in this list
        and present in the instance are returned.
        Otherwise, all attributes are returned.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance with values in json.

        json is a dictionary where keys are attribute names and values are attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
