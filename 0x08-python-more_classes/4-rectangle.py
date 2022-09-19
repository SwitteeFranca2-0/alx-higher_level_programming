#!/usr/bin/python3
"""This module defines a class rectangle"""


class Rectangle:
    """This class defines a rectangle"""


    def __init__(self, width=0, height=0):
        """This class initializes a clas
        Args:
            height: the height of a rectangle
            width: the width of a rectangle
        """

        self.height = height
        self.width = width

    @property
    def width(self):
    """This returns the private instance attribute"""
        return self.__width

    @property
    def height(self):
        """This returns the private instance attribute"""
        return self.__height

    @width.setter
    def width(self, value):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """The function defines the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self)
        """The function defines the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width + self.__height

    def __str__(self):
        """This functions defines the string attribute ofthe class"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
                if j == self.__width - 1:
                    print("")

    def __repr__(self):
        """This is to represent a rectangle"""
        return "Rectangle(" + self.__width + "," + self.__height + ")"

    def __eval__(self):
        
