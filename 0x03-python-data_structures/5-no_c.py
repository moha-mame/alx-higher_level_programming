#!/usr/bin/python3


def no_c(my_string):
    str_l = len(my_string)
    for idx in range(str_l - 1, -1, -1):
        if my_string[idx] == 'c' or my_string[idx] == 'C':
            if idx + 1 >= len(my_string):
                my_string = my_string[:idx]
            else:
                my_string = my_string[:idx] + my_string[idx + 1:]
    return my_string
