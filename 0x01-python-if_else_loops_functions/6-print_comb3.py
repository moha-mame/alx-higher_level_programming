#!/usr/bin/python3

for i in range(0, 10):
    for j in range(i, 10):
        if i != j:
            if i >= 10 - 2:
                print("{}{}".format(i, j))
                break
            print("{}{}, ".format(i, j), end='')
