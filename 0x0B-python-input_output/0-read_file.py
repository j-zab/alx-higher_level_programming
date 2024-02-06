#!/usr/bin/python3
"""Write a function that reads a text file & prints
it to the standard out without importing a module"""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
