#!/usr/bin/python3
"""Module Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """Return the dictionary represntation of data structure."""
    return obj.__dict__
