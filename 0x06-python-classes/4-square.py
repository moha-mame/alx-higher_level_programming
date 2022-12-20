#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""4-square.

This module implements the class square with a single
private instance attribute with the size of the square
and an instance method that returns its area.

Example:
        This module can be called from a main caller function like:

        Square = __import__('4-square').Square

        my_square = Square(89)
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))

        my_square.size = 3
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))

"""


class Square:
    """Class square

    This class has a single private instance attribute named "__size"
    __size, can be set and get as seen in the modules __doc__'s example.

    Attributes:
        __size (int): Size of the square.

    """

    def __init__(self, size=0):
        """__init__ method

        Initialize a new instance of class Square, taking an input as
        the size of the square.The input is set in the private attribute
        __size by calling its setter.

        Args:
            size (int): Value that represents the size of the square.

        """
        self.size = size

    def area(self):
        """Area of the square

        This public instance method returns the current square area
        """
        return self.__size ** 2

    @property
    def size(self):
        """Property size.

        Handles the private instance attribute size.

        When called to set the attribute, the input is validated
        as an int equals or greater than 0.

        For the setter:

        Args:
            size (int): Value that represents the size of the square.

        Raises:
            TypeError: If size is not and integer.
            ValueError: If size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
