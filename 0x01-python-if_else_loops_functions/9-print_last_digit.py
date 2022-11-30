#!/usr/bin/python3


def print_last_digit(number):
    last = abs(number) % 10
    print("{:d}".format(last), end='')
    return last
