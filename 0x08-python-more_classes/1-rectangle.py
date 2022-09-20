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
        """This functions returns a private property"""
        return self.__width

    @property
    def height(self):
        """his function returns a private property"""
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
