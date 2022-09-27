#!/usr/bin/python3
"""his module add a new object atribute"""


def add_attribute(obj, att, value):
    """Confirms the presenc of attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
