#!/usr/bin/python3


class Square:
    """Defines a square class"""

    def __init__(self, size=0):
        """Initializes the class by assigning values
        Args:
            size(int): size of square"""
        self.__size = size

    @property
    def size(self):
        """Returns values of attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets values of attribute size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns area of square"""
        return self.__size ** 2

    def my_print(self):
        """Prints value of squares with th e~ character"""
        for i in range(self.__size):
            for b in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
