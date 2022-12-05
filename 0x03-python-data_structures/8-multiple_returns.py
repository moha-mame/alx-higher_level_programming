#!/usr/bin/python3


def multiple_returns(sentence):

    out = [0, None]
    if sentence is not None:
        ls = len(sentence)
        if ls > 0:
            out[0] = ls
            out[1] = sentence[0]
    return tuple(out)
