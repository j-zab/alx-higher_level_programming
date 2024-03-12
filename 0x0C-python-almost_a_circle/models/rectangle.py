#!/usr/bin/python3
"""Defines a  new rectangle module (modules.rectangle)
to be used in the whole task"""
from models.base import Base


class Rectangle(Base):
    """Defines a new rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This Method initiliazes values for a rectangle object
        Args:
           width:The width size
           height: The height size
           x: Variable x
           y:  Variable y
        Return:
           Nothing Always
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # Getter and setter functs of the width
    @property
    def width(self):
        """Getter of width size
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter the width size
        Args:
           value: Size assigned to the width
        Return:
           Nothing Always
        """
        if type(value) is not int:
            raise TypeError("width must be an int")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    # Getter and setter of height
    @property
    def height(self):
        """Getter of the height size
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter of height size
        Args:
           value: Size assigned to the height
        Return:
           Nothing Always
        """
        if type(value) is not int:
            raise TypeError("height must be an int")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    # Getter and setter for  the x variable
    @property
    def x(self):
        """Getter of x variable
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Setter of the x variable
        Args:
           value: value assigned to the x variable
        Return:
           Nothing Always
        """
        if type(value) is not int:
            raise TypeError("x must be an int")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    # Getter and setter for the y variable
    @property
    def y(self):
        """Getter of y variable
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Setter of the y variable
        Args:
           value: value assigned to the y variable
        Return:
           Nothing Always
        """
        if type(value) is not int:
            raise TypeError("y must be an int")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """The Method that returns the area of the rectangle object
        Args:
           Not args
        Return:
           Area of the rectangle object
        """
        return self.width * self.height

    def display(self):
        """Method that prints the objects to  the stdout
           Rectangle object with the character#
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + self.width * '#')

    def __str__(self):
        """This Method overrides the str method
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                        self.y, self.width,
                                                        self.height))

    def update(self, *args, **kwargs):
        """The Method changes the order of args for rectangle object
        Args:
           *args: The list of args
           **kwargs: The Dictionary with args
        Return:
           Nothing Always
        """
        dict_order = ['id', 'width', 'height', 'x', 'y']
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
        """The Method returns a dictionary with
           attributes of the object.
        """
        dict_order = ['x', 'y', 'id', 'height', 'width']
        dict_attrs = {}
        for key in dict_order:
            dict_attrs[key] = getattr(self, key)
        return dict_attrs
