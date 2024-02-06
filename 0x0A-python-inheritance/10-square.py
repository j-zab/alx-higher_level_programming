#!/usr/bin/python3
"""Defines a Rectangle subclass/child Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Reps a square."""

    def __init__(self, size):
        """Initializes a new square from previous class.
        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
