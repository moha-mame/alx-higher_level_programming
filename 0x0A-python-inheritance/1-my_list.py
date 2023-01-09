#!/usr/bin/python3

""" 1-my_list module"""


class MyList(list):
    """ Subclass of list """

    def print_sorted(self):
        """ print_sorted function"""

        print(sorted(self))
