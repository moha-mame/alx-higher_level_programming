#!/usr/bin/python3
"""Module for append_after"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line
       containing a specific string
    """
    output = ''
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            output += line
            if search_string in line:
                output += new_string

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(output)
