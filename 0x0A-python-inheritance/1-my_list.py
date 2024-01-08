#!/usr/bin/python3
"""
containing MyList class
"""


class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """initializing the object"""
        super().__init__()

    def print_sorted(self):
        """printing the sorted list"""
        print(sorted(self))
