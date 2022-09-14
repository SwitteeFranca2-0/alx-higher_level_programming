#!/usr/usr/bin/python3


class Square:
    """Class defines a square"""

    def __init__(self, size=0):
        """Function returns value of size
        Args:
            size(int): The size of the square"""
        self.__size = size

    @property
    def size(self):
        """Function returns values of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Function sets value of size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Function finds area of square"""
        return self.__size ** 2
