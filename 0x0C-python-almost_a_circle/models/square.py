#!/usr/bin/python3
"""This module contain sthe class square."""
from .rectangle import Rectangle


class Square(Rectangle):
    """This class is the class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """This function inherits values from the super classes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """This function defines te str attribute"""
        square = "[Square] ({}) {}/".format(str(self.id), str(self.x))
        square += "{} - {}".format(str(self.y), str(self.width))
        return square

    @property
    def size(self):
        """This function returns the class atr"""
        return self.width

    @size.setter
    def size(self, val):
        super().width
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """This function updates the value of the attributes of the class"""
        no_args = 0
        if args and len(args) != 0:
            for arg in args:
                if arg is None:
                    self.__init__(self.id, self.width, self.height,
                                  self.x, self.y)
                else:
                    if no_args == 0:
                        self.id = arg
                    elif no_args == 1:
                        self.size = arg
                    elif no_args == 2:
                        self.x = arg
                    elif no_args == 3:
                        self.y = arg
                no_args += 1
        else:
            [setattr(self, k, v) for k, v in
                kwargs.items() if hasattr(self, k)]

    def to_dictionary(self):
        """his returns the dictionary representation of the class"""
        return {
            'id': self.id, 'x': self.x,
            'size': self.size, 'y': self.y
        }
