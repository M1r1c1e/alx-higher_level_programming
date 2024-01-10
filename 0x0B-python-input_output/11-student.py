#!/usr/bin/python3
"""Defining a class Student."""


class Student:
    """Representing a student."""

    def __init__(self, first_name, last_name, age):
        """the first introduction a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieving a dictionary representation of the Student.

        If attrs is a list of strings, representing exclusively those attributes
        included in the list.

        Args:
            attrs (list): (Optional) The represented attributes.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replacing all attributes of a Student.

        Args:
            json (dict): replacing attributes with key or value pairs
        """
        for k, v in json.items():
            setattr(self, k, v)
