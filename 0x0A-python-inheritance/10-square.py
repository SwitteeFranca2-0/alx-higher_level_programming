#!/usr/bin/python3
"""This module creates abse geometry """


class BaseGeometry:
    """Declaring a class"""

    def area(self):
        """Defining the area of the class"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This function validates ntegers"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """This class declares a rectangle"""

    def __init__(self, width, height):
        """This functin nitialises a class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """This function reutns the area"""
        return self.__height * self.__width

    def __str__(self):
        """This returns a striing of the class"""
        rec = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return rec


class Square(Rectangle):
    """This declares a square class"""

    def __init__(self, size):
        """This function initialises the class"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
