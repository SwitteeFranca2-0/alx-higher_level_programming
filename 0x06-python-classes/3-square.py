#!/usr/bin/python3


class Square:
    """
        class defining a square.
        """

    def __init__(self, size=0):
        """Initializig the size and including sme conditionals
        Args:
            size(int): The size of the square"""

        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """return the area of a square"""

        return self.__size ** 2
