#!/usr/bin/python3
"""function to find the max integer in a list
"""


def max_integer(list=[]):
    """the function that finds and return the max integer in a list of integers
        function should return non if list is empty
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
