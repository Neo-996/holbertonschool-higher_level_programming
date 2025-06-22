#!/usr/bin/python3
"""Convert CSV data to JSON."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV file to JSON file named 'data.json'.

    Args:
        csv_filename (str): Path to the CSV file.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        with open(csv_filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)
        with open("data.json", "w", encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)
        return True
    except Exception:
        return False
