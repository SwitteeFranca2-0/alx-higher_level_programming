#!/usr/bin/python3
"""This module decalres a class"""


class MyList(list):
    """This class inherits from a class list."""

    def __init__(self):
        """Initializes the object"""
        super().__init__()

    def print_sorted(self):
        """print the sorted list"""
        print(sorted(self))
