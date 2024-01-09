#!/usr/bin/python3
"""Returning an instance of a specific class."""


def is_same_class(obj, a_class):
    """Checking if object is an instance of a given class.
    Args:
        obj (any): The object to be checked.
        a_class (type): The class compared to the type of object
    Returns:
        Boolean of an instance of a_class.
    """
    if type(obj) == a_class:
        return True
    return False
