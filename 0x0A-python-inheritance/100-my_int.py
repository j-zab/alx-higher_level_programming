#!/usr/bin/python3
"""Writes a class MyInt to inherits from int."""


class MyInt(int):
    """Flips int operators == and !=."""

    def __eq__(self, value):
        """Replaces == operator with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Replaces != operator with == behavior."""
        return self.real == value
