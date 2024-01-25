#!/usr/bin/python3
"""
The module function is to  add up 2 integers
"""


def add_integer(a, b=98):
    """Returns the sum of 2 integers or floats as integers
    Args:
        a: the first argument
        b: the second argument
    Returns:
        The sum of the 2 arguments
    Raises:
        TypeError: If either of the arguments not an integer or a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
