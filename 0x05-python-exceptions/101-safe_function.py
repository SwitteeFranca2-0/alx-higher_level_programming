#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except sys.exc_info()[0]:
        print("Exception: ", sys.exc_info()[1], file=sys.stderr)
        return None
    return res
