#!/usr/bin/python3
"""This module cntains the read_file"""


def read_file(filename=""):
    """This implements the read line"""
    with open(filename) as f:
        [print(line, end="") for line in f]
    print("")
