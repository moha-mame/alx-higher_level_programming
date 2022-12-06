#!/usr/bin/python3

if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div
    import sys

    inp = sys.argv
    l_inp = len(inp)
    ops = ['+', '-', '*', '/']
    if l_inp != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif inp[2] not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        op = sys.argv[2]
        if op == '+':
            print("{} {} {} = {}".format(a, op, b, add(a, b)))
        elif op == '-':
            print("{} {} {} = {}".format(a, op, b, sub(a, b)))
        elif op == '*':
            print("{} {} {} = {}".format(a, op, b, mul(a, b)))
        elif op == '/':
            print("{} {} {} = {}".format(a, op, b, div(a, b)))
        else:
            pass
