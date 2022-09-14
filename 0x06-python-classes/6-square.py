#!/usr/bin/python3
"""Defining a square cllass"""


class Square:
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the class square and attribute
        Args:
            size(int): size of the square
            position: position cooordinateswhere the square is to be pronted
            """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Returns value of property size"""
        return self.__size

    @property
    def position(self):
        """Returns value of attribute position"""
        return self.__position

    @size.setter
    def size(self, value):
        """Sets value of iiattribute size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        "Sets value of the attribute, position"
        if (type(value) is not tuple or len(value) != 2 or
                all(type(num for num in value) is not int or 
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints value of square with the "#" character"""
        for i in range(self.__position[1]):
            print(" ")
        for i in range(self.__size):
            if self.__position and self.__position[1] <= 1:
                for c in range(self.__position[0]):
                    print(" ", end="")
            for b in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
            return
