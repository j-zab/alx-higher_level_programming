#!/usr/bin/python3
"""Defines the object attribute and methods by using the
lookup function."""


def lookup(obj):
    """Returns the list of an object's present attributes and methods."""

    return (dir(obj))
