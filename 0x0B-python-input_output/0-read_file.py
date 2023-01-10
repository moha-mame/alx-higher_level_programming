#!/usr/bin/python3

""" read_file module """


def read_file(filename=""):
    """
    read_file function

    reads a text file (UTF8) and prints it to stdout
    """

    with open(filename, mode='r', encoding='utf-8') as f:
        print(f.read(), end='')
