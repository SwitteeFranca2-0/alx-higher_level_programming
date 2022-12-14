#!/usr/bin/python3
"""Defining a class, magic class"""

import math


class MagicClass:
    """class magic class"""

    def __init__(self, radius=0):
        """initialises the circle
        Args:
            radius(int): radius of circle"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Returns the area of circle"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Returns the circumference of the circle"""
        return 2 * math.pi * self.__radius
