#!/usr/bin/python3
"""Thiis module defines a class student"""


class Student:
    """hsi defines a class student"""

    def __init__(self, first_name, last_name, age):
        """This function intialises tha class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary of itself"""
        return self.__dict__
