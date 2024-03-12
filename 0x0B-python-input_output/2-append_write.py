#!/usr/bin/python3
"""Writes a string at the end of a text file (UTF8)
& returns the # of chars added"""


def append_write(filename="", text=""):
    """Appends a str to the end of a UTF8 text file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
