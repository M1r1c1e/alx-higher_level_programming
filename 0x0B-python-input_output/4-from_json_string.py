#!/usr/bin/python3
"""Defining a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Returnng the Python object representatingg a JSON string."""
    return json.loads(my_str)
