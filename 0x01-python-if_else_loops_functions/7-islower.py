#!/usr/bin/python3


def islower(c):
    if ord(c[0]) < ord('a') or ord(c[0]) > ord('z'):
        return False
    return True
