#!/usr/bin/python3
"""Defining a square class"""


class Square:
    """
        class defining a square.
        """

    def __init__(self, size=0):
        """Initializig the size and including sme conditionals

        Args:
            size(int): size of the square."""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
