#!/usr/bin/python3


if __name__ == "__main__":
    """my calculation"""

    from calculator_1 import add, mul, div, sub
    from sys import argv

    if (len(argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = agrv[1]
    b = argv[3]

    if (argv[2] == '+'):
        print("{} + {} = {}".format(a, b, add(int(a), int(b))))
    elif(argv[2] == '-'):
        print("{} - {} = {}".format(a, b, sub(int(a), int(b))))
    elif(argv[2] == '*'):
        print("{} * {} = {}".format(a, b, mul(int(a), int(b))))
    elif(argv[2] == '/'):
        print("{} / {} = {}".format(a, b, div(int(a), int(b))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
