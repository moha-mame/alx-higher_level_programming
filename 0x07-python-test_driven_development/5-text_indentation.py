#!/usr/bin/python3
"""5-text_indentation module

This module holds only one function that prints a text with 2 new lines
after each of these characters:

., ? and :

"""


def text_indentation(text):
    """text_indentation function

    text_indentation(text)

    Only recieves a string as an input, otherwise a TypeError is rised.

    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    new = 1
    for c in text:
        if new != 0 and c == ' ':
            continue
        new = 0
        print(c, end='')
        if c in ['.', '?', ':']:
            new = 1
            print("\n")
