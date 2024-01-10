#!/usr/bin/python3
"""Defining a class Student."""


class Student:
    """Representing a student."""

    def __init__(self, first_name, last_name, age):
        """New Student initializtion

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """student dictionary representation.

        Args:
            attrs (list): (Optional) The attributes represented.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
