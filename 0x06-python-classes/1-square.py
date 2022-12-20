#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""1-square.

This module implements the class square with a single
private instance attribute.

Example:
        This module can be called from a main caller function like:

        Square = __import__('1-square').Square

        my_square = Square(3)
        print(type(my_square))
        print(my_square.__dict__)
"""


class Square:
    """Class square

    This class has a single private instance attribute named "__size"

    Attributes:
        __size (int): Size of the square.

    """
    def __init__(self, size):
        """__init__ method

        Initialize a new instance of class Square, taking an input as
        the size of the square.

        Args:
            size (): private instance attribute that represents the size
                     of the square.

        """
        self.__size = size
