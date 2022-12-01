#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    inp = sys.argv
    l_inp = len(inp)
    if l_inp == 1:
        print("0 arguments.")
        exit()
    elif l_inp == 2:
        print("1 argument:")
        print("1: {}".format(inp[1]))
    else:
        print("{:d} arguments:".format(l_inp - 1))
        for idx, i in enumerate(inp[1:]):
            print("{:d}: {}".format(idx + 1, i))
