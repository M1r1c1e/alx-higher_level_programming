#!/usr/bin/python3
"""Defining an inherited list class MyList."""


class MyList(list):
    """Implementing the sorted prints for the built-in list class."""

    def print_sorted(self):
        """Print a list in an ascending order which is sorted."""
        print(sorted(self))
