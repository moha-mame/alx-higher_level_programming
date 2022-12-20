#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""5-square.

This module only implements the class square with a single
private instance attribute holding the size of the square.
There's a method that returns its area, and one that prints
the square using #'s

Example:
        This module can be called from a main caller function like:
        Square = __import__('5-square').Square

        my_square = Square(3)
        my_square.my_print()

"""


class Square:
    """Class square

    This class has a single private instance attribute named "__size"
    __size, can be set and get as seen in the modules __doc__'s example.

    Methods implemented as "area" returning the current area of the square
    and "my_print" that prints the square using the symbol #.

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

    def my_print(self):
        """Print the square

        This method uses the symbol # to graphically represent the
        current square state.

        """
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            if i < self.__size - 1:
                print()
        print()

    @property
    def size(self):
        """Property size.

        Handles the private instance attribute size.

        When called to set the attribute, the input is validated
        as an int equals or greater than 0.

        For the setter:

        Args:
            value (int): Value that represents the size of the square.

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
