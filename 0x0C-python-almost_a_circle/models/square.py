#!/usr/bin/python3
"""The Module that defines a new square object
To be used throught the code"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a new square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """This method initializes the new square
        Args:
           size: The square's side size
           x: Position on x axis.
           y: The Position on the y axis.
        Return:
           Nothing Always
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """The Method returns a str"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.width))

    @property
    def size(self):
        """Getter of the square size
        """
        return self.width

    @size.setter
    def size(self, value):
        """Setter of the square size
        Args:
           value: Size to assign
        Return:
           Nothing always
        """
        self.width = value
        self.heigth = value

    def update(self, *args, **kwargs):
        """The Method updates the args for the square object
        Args:
           *args: list of args
           **kwargs: The Dictionary of the args.
        Return:
           Nothing always
        """
        dict_order = ['id', 'size', 'x', 'y']
        if args is not None and bool(args) is True:
            i = 0
            for key in dict_order:
                try:
                    setattr(self, key, args[i])
                except IndexError:
                    pass
                i += 1
        else:
            for key in dict_order:
                try:
                    setattr(self, key, kwargs[key])
                except KeyError:
                    pass

    def to_dictionary(self):
        """The Method returns the dictionary
           representation of the defined Square.
        """
        dict_order = ['id', 'x', 'size', 'y']
        dict_attrs = {}
        for key in dict_order:
            dict_attrs[key] = getattr(self, key)
        return dict_attrs
