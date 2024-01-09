#!/usr/bin/python3
"""Defining a function attributes."""


def add_attribute(obj, att, value):
    """Adding a new attribute to an object if possible.
    Raises:
        TypeError: If function cannot add atribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
