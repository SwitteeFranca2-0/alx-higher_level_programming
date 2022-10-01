#!/usr/bin/python3
"""This module contains the class rectangle"""
from base import Base


class Rectangle(Base):
    """This class is the class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This function ntialises the class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns priivate instance of attribute"""
        return self.__width

    @property
    def height(self):
        """Returns priivate instance of attribute"""
        return self.__height

    @property
    def x(self):
        """Returns priivate instance of attribute"""
        return self.__x

    @property
    def y(self):
        """Returns priivate instance of attribute"""
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This function eturns the area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """This function prints in stdoutt the recrangle instance"""
        [print("") for i in range(self.__y)]
        for i in range(self.__height):
            [print(" ", end="") for b in range(self.__x)]
            [print('#', end="") for j in range(self.__width)]
            print("")

    def __str__(self):
        """Defines the str attribut of the clas"""
        rec = "[Rectangle] ({}) {}/".format(str(self.id), str(self.__x))
        rec += "{} - {}/".format(str(self.__y), str(self.__width))
        rec += "{}".format(str(self.__height))
        return rec

    def update(self, *args, **kwargs):
        """This function updates the class attributes"""
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
                        self.__width = arg
                    elif no_args == 2:
                        self.__height = arg
                    elif no_args == 3:
                        self.__x = arg
                    elif no_args == 4:
                        self.__y = arg
                no_args += 1
        else:
            [setattr(self, k, v) for k, v in
                kwargs.items() if hasattr(self, k)]

    def to_dictionary(self):
        """This returns the dictionary representation of the class"""
        return {k.split("__")[-1]: v for k, v in self.__dict__.items()}
