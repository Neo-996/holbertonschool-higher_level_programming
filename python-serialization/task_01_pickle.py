#!/usr/bin/python3
"""Serialization and deserialization using pickle for a custom object."""

import pickle


class CustomObject:
    """Custom class for demonstrating pickle serialization."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print object attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize this instance to the specified file."""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            pass  # Optional: log or print error if needed

    @classmethod
    def deserialize(cls, filename):
        """Deserialize from file and return a CustomObject instance."""
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
        except Exception:
            return None
