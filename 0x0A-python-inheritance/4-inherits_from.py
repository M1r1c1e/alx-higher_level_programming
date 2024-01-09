#!/usr/bin/python3
"""Defining an inherited class-checking method."""


def inherits_from(obj, a_class):
    """Checking if an object is an inherited instance of a class.
    Args:
        obj (any): The object to be check.
        a_class (type): The class to be compared.
    Returns:
        The boolean of inheritance.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
