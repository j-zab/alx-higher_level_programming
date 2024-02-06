#!/usr/bin/python3
"""Defines a class-checking function
that returns "TREU" if the inherited class matches"""


def is_same_class(obj, a_class):
    """Checks if object is an instance of a class,
    Return true if object is an instance of the
    class, otherwise return false"""
    return (type(obj) == a_class)
