#!/usr/bin/python3


def weight_average(my_list=[]):

    if len(my_list) == 0:
        return 0

    div = 0
    pond = 0
    for pair in my_list:
        pond = pond + (pair[0] * pair[1])
        div = div + pair[1]
    pond = pond / div
    return pond
