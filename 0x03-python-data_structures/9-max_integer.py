#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    big = my_list[0]
    for n in my_list:
        if n > big:
            big = n
    return big
