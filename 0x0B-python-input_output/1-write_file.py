#!/usr/bin/python3
"""his module contains the customised write function"""


def write_file(filename="", text=""):
    """This function defines a "write_file"""
    with open(filename, 'w', encoding="utf-8") as f:
        nb = f.write(text)
    return nb
