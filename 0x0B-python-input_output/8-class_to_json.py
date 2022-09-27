#!/usr/bin/python3
"""This module has the 'class to json' function"""


def class_to_json(obj):
    """This returns the dictionary of the 'obj' field"""
    return obj.__dict__
