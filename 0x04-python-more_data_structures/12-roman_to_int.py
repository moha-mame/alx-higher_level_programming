#!/usr/bin/python3


def roman_to_int(roman_string):

    if roman_string is None or type(roman_string) != str:
        return 0

    roman_dict = {
        'I': 1, 'V': 5,
        'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000}

    num = 0
    r_digt = 0
    prev = 0
    count = 0
    for N in reversed(roman_string):
        r_digt = roman_dict[N]
        if r_digt >= prev:
            num += r_digt
        elif r_digt < prev:
            num -= r_digt
        prev = r_digt

    return num
