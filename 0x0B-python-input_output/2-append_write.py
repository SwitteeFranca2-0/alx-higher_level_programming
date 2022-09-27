#!usr/bin/python3
"""This module contains the append function"""


def append_write(filename="", text=""):
    """Thiis function is an append function"""
    with open(filename, 'a', encoding="utf-8") as f:
        nb = f.write(text)
    return nb
