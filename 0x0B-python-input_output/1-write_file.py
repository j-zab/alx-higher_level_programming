#!/usr/bin/python3
"""Writes a function that writes a string to a text file (UTF8) &
returns the number of characters written"""


def write_file(filename="", text=""):
    """Write a str to a UTF8 text file.
    Args:
        filename (string): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The # of chars written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
