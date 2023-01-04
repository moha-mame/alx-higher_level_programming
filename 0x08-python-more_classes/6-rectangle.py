#!/usr/bin/python3

""" 0-rectangle module

"""


class Rectangle:
    """ Rectangle Class

    Class defining a rectangle

    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """__init__

        Initializing instance of a rectangle
        private instance attributes: width and height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """similar as my_print"""
        msg = []
        if self.__width > 0 and self.__height > 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    msg.append("#")
                if i < self.__height - 1:
                    msg.append('\n')
        return ''.join(msg)

    def __repr__(self):
        m = "{}({}, {})"
        return(m.format(self.__class__.__name__, self.__width, self.__height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def my_print(self):
        """Print the square
        This method uses the symbol # to graphically represent the
        current square state.
        """
        if self.__width > 0 and self.__height > 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    print("#", end='')
                if i < self.__height - 1:
                    print()
        print()
