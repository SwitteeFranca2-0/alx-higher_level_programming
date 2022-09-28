#!/usr/bin/python3
"""his module contains the 'append_after' function"""


def append_after(filename="", search_string="", new_string=""):
    """The append after a search string functiion"""
    lines = ""
    with open(filename) as f:
        for line in f:
            lines += line
            if search_string in line:
                lines += new_string
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(lines)
