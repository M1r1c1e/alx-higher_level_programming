#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """Writing a string to a UTF8 text file.

    Args:
        filename (str): The file's name to be written
        text (str): The text to write to the file.
    Returns:
        The total number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
