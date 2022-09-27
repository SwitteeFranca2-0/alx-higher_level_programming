#!/usr/bin/python3
"""This module creates abse geometry """


class BaseGeometry:
    """Declaring a class"""

    def area(self):
        """Defining the area of the class"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This function validates an integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """This declares a Rectangle"""

    def __init__(self, width, height):
        """Thiis function initialises a rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Defining the area of the class"""
        return self.__height * self.__width

    def __str__(self):
        """This function validates ntegers"""
        rec = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return rec
