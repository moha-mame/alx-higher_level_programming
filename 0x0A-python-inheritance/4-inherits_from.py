#!/usr/bin/python3

""" inherints_from module """


def inherits_from(obj, a_class):
    """ inherits_from function """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
