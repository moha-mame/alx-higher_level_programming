#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    la = len(tuple_a)
    lb = len(tuple_b)
    idx = 0
    res = [0, 0]
    while idx < 2:
        if idx < la:
            res[idx] += tuple_a[idx]
        if idx < lb:
            res[idx] += tuple_b[idx]
        idx += 1

    return tuple(res)
