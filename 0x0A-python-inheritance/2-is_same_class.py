#!/usr/bin/python3

""" is_same_class module"""


def is_same_class(obj, a_class):
    """ is_same_class function """

    return type(obj).__name__ == a_class.__name__
