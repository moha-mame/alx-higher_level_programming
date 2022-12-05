#!/usr/bin/python3


def divisible_by_2(my_list=[]):

    is_div = []

    if len(my_list) == 0:
        return is_div

    is_div = [True if n % 2 == 0 else False for n in my_list]
    return is_div
