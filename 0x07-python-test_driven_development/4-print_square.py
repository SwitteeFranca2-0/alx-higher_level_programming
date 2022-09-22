#!/usr/bin/python3
"""module prints square"""


def print_square(size):
    """This function prints  squares
        Args:
            size(int): size of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    if size == 0:
        return

    for i in range(size):
        for j in range(size):
            print("#", end="")
            if j == size - 1:
                print("")
