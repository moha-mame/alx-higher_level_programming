#!/usr/bin/python3

""" number_of_lines module """


def number_of_lines(filename=""):
    """
    number_of_lines function

    returns the number of lines of a text file.
    """

    with open(filename, mode='r', encoding='utf-8') as f:
        lines = len(f.readlines())
        return lines
