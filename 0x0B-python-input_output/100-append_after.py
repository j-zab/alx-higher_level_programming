#!/usr/bin/python3
"""Writes a mudule that permit a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a given str in a file.
    Args:
        filename (str): The file name
        search_string (str): The str to search for within the file.
        new_string (str): The str to insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
