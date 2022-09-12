#!/usr/bin/python3
import sys


def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += (a ** b) / i
        except sys.exc_info()[0]:
            result = a + b
            break
    return result
