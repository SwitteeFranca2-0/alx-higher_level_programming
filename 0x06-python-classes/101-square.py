#!/usr/bin/python3


class Square:
    """Defining a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initaialsng the squer:
        Args:
            size(int): size of the shape."
            poosition(int, int): position cordinates of square"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Returns size of suare when requested"""
        return self.__size

    @property
    def position(self):
        """Returns position of square when requested"""
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns area of shape"""
        return self.__size ** 2

    def my_print(self):
        """Printd the square with spaces an dhash tags"""
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

    def __str__(self):
        """Defines the string  method of the class"""
        for i in range(self.__position[1]):
            print(" ")
        for i in range(self.__size):
            if self.__position and self.__position[1] <= 1:
                for c in range(self.__position[0]):
                    print(" ", end="")
            for b in range(self.__size):
                print("#", end="")
            if i != self.__size - 1:
                print("")
        if self.__size == 0:
            print("")
        return ("")
