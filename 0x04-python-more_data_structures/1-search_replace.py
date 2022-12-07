#!/usr/bin/python3


def search_replace(my_list, search, replace):
    if my_list is None:
        return
    new = my_list[:]
    for idx, c in enumerate(new):
        if c == search:
            new[idx] = replace
    return new
