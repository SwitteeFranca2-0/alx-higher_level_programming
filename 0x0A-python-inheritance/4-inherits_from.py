#!/usr/bin/python3
"""This module shows if sub class of or not"""


def inherits_from(obj, a_class):
    """This functions checks if subclass or not"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
