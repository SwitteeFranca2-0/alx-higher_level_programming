#!/usr/bin/python3
""" Print last number of  a value"""


def print_last_digit(number):
    if (number < 0):
        number = number * -1
    print(number % 10, end="")
    return number % 10
