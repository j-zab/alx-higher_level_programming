#!/usr/bin/python3
"""my square module."""


class Square:
    """defines a Square in the class."""

    def __str__(self):
        """teach python to print the square my way"""
        return self.pos_print()[:-1]

    def __init__(self, size=0, position=(0, 0)):
        """ initialize the square int he class
        Args:
            size: one  side of a square
            position: the cordinates of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """The length of a side of square
        Raises:
            TypeError: if size isnt an integer
            ValueError: if size is < 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ the size of e square inthe class
        Args:
            value: the size of the square
        Raises:
                TypeError: if value isnt interger
                ValueError: if value of the square is  < 0
        """
        if not isinstance(value, int):
            raise TypeError('size of e square must be an int')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """property of the position of the square
        Raises:
            TypeError: if value != tuple of 2 ints >= 0.
        Returns: the position of the size
        """
        return self.__position

    @position.setter
    def position(self, value):
        """set the position
        Args:
            value: where
        Raises:
                TypeError: if not tuple, ints, positive
        Returns: the position
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 +ve ints')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 +ve ints')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 +ve ints')
        self.__position = value

    def area(self):
        """ the area of square
        Returns:
            size * size
        """
        return self.__size * self.__size

    def pos_print(self):
        """returns the printed square with position"""
        pos = ""
        if not self.size:
            return "\n"
        for w in range(self.position[1]):
            pos += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """print square."""
        print(self.pos_print(), end="")
