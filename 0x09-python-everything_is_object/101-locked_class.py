#!/usr/bin/python3
"""This module defines a class"""


class LockedClass:
    """This is a locked class"""

    __slots__ = ['first_name']

    def __init__(self, first_name=""):
        """This function says a name
            Args:
                frist_name: name
                """
        self.first_name = first_name
