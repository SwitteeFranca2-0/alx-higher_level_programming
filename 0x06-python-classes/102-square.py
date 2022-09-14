#!/usr/usr/bin/python3
"""Class square defining"""


class Square:
    """Initializing the square"""

    def __init__(self, size=0):
        """Initializing the square.
        Args:
            size(int): size of the square."""
        self.size = size

    @property
    def size(self):
        """Returns the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of square"""
        return self.__size ** 2

    def __gt__(self, other):
        """Defines the comparison >"""
        return self.area() > other.area()

    def __lt__(self, other):
        """Defines the comparision <"""
        return self.area() < other.area()

    def __le__(self, other):
        """Defines the comparison >="""
        return self.area() <= other.area()

    def __eq__(self, other):
        """Defines the ci=omparisoni =="""
        return self.area() == other.area()

    def __ne__(self, other):
        """Defines the comparisom !="""
        return self.area() != other.area()

    def __ge__(self, other):
        """Defines the comparison >="""
        return self.area() >= other.area()
