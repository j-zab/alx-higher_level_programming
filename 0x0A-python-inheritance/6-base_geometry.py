#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry
that raises the base on Exception with the message
area() is not implemented"""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")
