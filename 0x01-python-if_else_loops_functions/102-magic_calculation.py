#!/usr/bin/python3
"""Magic calculation"""


def m(a, b, c):
    if (a < b):
        return c
    if (c > b):
        return a + b
    return a * b - c
