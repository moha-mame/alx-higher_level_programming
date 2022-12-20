#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""6-square.

This module only implements the class square with two private
instance attributes holding the size and the position of the square.
There's a method that returns its area, and one that prints
the square using #'s

Example:
        This module can be called from a main caller function like:

        Square = __import__('6-square').Square

        my_square_1 = Square(3)
        my_square_1.my_print()

        print("--")

        my_square_2 = Square(3, (1, 1))
        my_square_2.my_print()
"""


class Square:
    """Class square

    This class has a single private instance attribute named "__size"
    __size, can be set and get as seen in the modules __doc__'s example.

    Methods implemented as "area" returning the current area of the square
    and "my_print" that prints the square using the symbol #.

    Attributes:
        __size (int): Size of the square.
        __position (:tuple:`int`): (x, y) position of the square

    """

    def __init__(self, size=0, position=(0, 0)):
        """__init__ method

        Initialize a new instance of class Square, taking the first input as
        the size of the square, and the second input.Every input is set
        in their respective private attribute by calling their setter.

        Args:
            size (int): Value that represents the size of the square.
            __position (:tuple:`int`): (x, y) position of the square.

        """
        self.size = size
        self.position = position

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
        if self.__size > 0:
            for k in range(self.__position[1]):
                print()

            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end='')
                for j in range(self.__size):
                    print("#", end='')
                if i < self.__size - 1:
                    print()
        print()

    @property
    def position(self):
        """Property position.

        Handles the private instance attribute position.

        When called to set the attribute, the input is validated
        as a tuple of 2 positive integers.

        For the setter:

        Args:
            value (:tuple:`int`): (x, y) position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.

        """
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
                    return
        raise TypeError("position must be a tuple of 2 positive integers")

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
