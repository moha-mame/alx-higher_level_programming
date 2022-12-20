#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""2-square.

This module implements the class square with a single
private instance attribute. Instantiation will evaluate
a correct input value.

Example:
        This module can be called from a main caller function like:

        Square = __import__('2-square').Square

        my_square_1 = Square(3)
        print(type(my_square_1))
        print(my_square_1.__dict__)
"""


class Square:
    """Class square

    This class has a single private instance attribute named "__size"
    of type int.

    Attributes:
        __size (int): Size of the square.

    """

    def __init__(self, size=0):
        """__init__ method

        Initialize a new instance of class Square, taking an input as
        the size of the square. The input is validated as an int equals
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
