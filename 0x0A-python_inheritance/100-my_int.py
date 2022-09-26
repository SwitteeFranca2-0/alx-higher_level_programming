#!/usr/bin/python3
"""This modulle introduces a new class"""


class MyInt(int):
    """This class returns the invert of the assigned bool"""

    def __eq__(self, other):
        """hiis function evaluates """
        return self.real != other

    def __ne__(self, other):
        """This function evaluates"""
        return self.real == other
