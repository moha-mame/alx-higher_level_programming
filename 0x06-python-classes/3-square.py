#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""3-square.

This module implements the class square with a single
private instance attribute with the size of the square
and an instance method that returns its area.

Example:
        This module can be called from a main caller function like:

        Square = __import__('3-square').Square

        my_square_1 = Square(3)
        print("Area: {}".format(my_square_1.area()))

"""


class Square:
    """Class square

    This class has a private instance attribute named "__size" and
    a public instance method named "area" that returns the area of
    the square.

    Attributes:
        __size (int): Size of the square.

    """
    def __init__(self, size=0):
        """__init__ method

        Initialize a new instance of class Square, taking an input as
        the size of the square.The input is validated as an int equals
        or greater than 0.

        Args:
            size (int): Value that represents the size of the square.

        Raises:
            TypeError: If size is not and integer.
            ValueError: If size is less than 0.

        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Area of the square

        This public instance method returns the current square area
        """
        return self.__size ** 2
