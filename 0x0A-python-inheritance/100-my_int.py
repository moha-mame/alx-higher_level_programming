#!/usr/bin/python3

""" 100-my_int module """


class MyInt(int):
    """ MyInt class """

    def __eq__(self, some_int):
        return not super().__eq__(some_int)

    def __ne__(self, some_int):
        return not super().__ne__(some_int)
