#!/usr/bin/python3
"""Defining a function a function that insert a text in a file."""


def append_after(filename="", search_string="", new_string=""):
    """Insertin text continiously at the next line containing a given string in a file.
    Args:
        filename (str): The file's name.
        search_string (str): The string to look for within the file.
        new_string (str): The inserted string.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
