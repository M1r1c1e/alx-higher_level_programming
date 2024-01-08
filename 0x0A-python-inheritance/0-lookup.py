#!/usr/bin/python3
"""Defining the object attribute lookup function."""


def lookup(obj):
    """Returning a list of available object attributes."""
    return (dir(obj))
