#!/usr/bin/python3
"""Defining a class Student."""


class Student:
    """Representing a student."""

    def __init__(self, first_name, last_name, age):
        """New Student initialization.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Student dictionary representation."""
        return self.__dict__
