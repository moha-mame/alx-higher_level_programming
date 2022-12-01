#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    sum = 0
    inp = sys.argv
    l_inp = len(inp)
    if l_inp > 1:
        for i in inp[1:]:
            sum = sum + int(i)
    print(sum)
