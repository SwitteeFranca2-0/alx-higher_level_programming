#!/usr/bin/python3
"""Thiis module defines a class student"""


class Student:
    """hsi defines a class student"""

    def __init__(self, first_name, last_name, age):
        """This function intialises tha class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary of itself"""
        if type(attrs) == list and all(type(n) is str for n in attrs):
            return {a: k for a, k in self.__dict__.items() if a in attrs}
        return self.__dict__
