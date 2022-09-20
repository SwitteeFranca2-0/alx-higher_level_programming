#!/usr/bin/python3
"""This module defines a class rectangle"""


class Rectangle:
    """This class defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """This class initializes a clas
        Args:
            height: the height of a rectangle
            width: the width of a rectangle
        """

        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        """This returns the private instance attribute"""
        return self.__width

    @property
    def height(self):
        """This returns the private instance attribute"""
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """The function defines the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """The function defines the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__width + self.__height)

    def __str__(self):
        """This functions defines the string attribute ofthe class"""
        rec = []
        if self.__width == 0 or self.__height == 0:
            return ("")
        for i in range(self.__height):
            [rec.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rec.append("\n")
        return ("").join(rec)

    def __repr__(self):
        """This is to represent a rectangle"""
        rec = "Rectangle(" + str(self.__width) + ","
        rec += str(self.__height) + ")"
        return rec

    def __del__(self):
        """Deletes a instnace class"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """his function identifies whether or not bith triangles are equal"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Making a square is the use of this function"""
        return cls(size, size)
