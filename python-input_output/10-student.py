#!/usr/bin/python3
"""
Module defining the Student class with selective JSON serialization.
"""

class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes named in this list
        that exist in the instance are included.
        Otherwise, all attributes are returned.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            # Filter only attributes in attrs and present in instance __dict__
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        # Return all attributes
        return self.__dict__.copy()
