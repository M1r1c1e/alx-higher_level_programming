#!/usr/bin/python3
"""Defining a file-appending function."""


def append_write(filename="", text=""):
    """Appending a string to the end of a UTF8 text file.

    Args:
        filename (str): The name of the file appending to.
        text (str): The string that is appending to the file.
    Returns:
        The number or amount of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
