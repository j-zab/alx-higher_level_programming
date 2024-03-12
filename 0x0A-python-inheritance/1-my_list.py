#!/usr/bin/python3
"""Defines the subclass or child list in the class MyList."""


class MyList(list):
    """This class is a subclass of the list class."""

    def print_sorted(self):
        """Print a sorted list in a pattern."""
        print(sorted(self))
