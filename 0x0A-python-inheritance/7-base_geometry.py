#!/usr/bin/python3
"""This module creates abse geometry """


class BaseGeometry:
    """Declaring a class"""

    def area(self):
        """Defining the area of the class"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
