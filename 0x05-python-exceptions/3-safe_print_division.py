#!/usr/bin/python3


def safe_print_division(a, b):
    d = 0
    try:
        d = a / b
    except:
        d = None
    finally:
        print("Inside result: {}".format(d))
        return d
