#!/usr/bin/python3
"""the module prints a text"""


def text_indentation(text):
    """Text indentation based on some given characters
        Args:
            text: a group of words to edit.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for t in text:
        print(t, end="")
        if t == "." or t == "?" or t == ":":
            print("")
            print("")
