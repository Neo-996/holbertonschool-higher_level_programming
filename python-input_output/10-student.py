#!/usr/bin/python3
"""Student class with serialization support."""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Init attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dict repr of instance.

        If attrs is a list of strings, return only matching keys.
        """
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            return {
                k: getattr(self, k)
                for k in attrs if hasattr(self, k)
            }
        return self.__dict__
