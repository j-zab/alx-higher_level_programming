#!/usr/bin/python3
"""Defines function to ckeck for inherited class."""


def inherits_from(obj, a_class):
    """ Args:
    obj (any): The object to check if its inherited
    a_class (type): The class used to match the type of obj to

    Returns "true" if object is an instance of a class that inherited
    (directly or indirectly) from the specified class
    and "False" if not
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
