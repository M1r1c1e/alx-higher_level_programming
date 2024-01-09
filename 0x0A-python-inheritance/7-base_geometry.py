#!/usr/bin/python3
"""Defining class BaseGeometry."""


class BaseGeometry:
    """Class body."""

    def area(self):
        """is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validating a parameter format.
            TypeError: If the value is not an integer.
            ValueError: If the value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
