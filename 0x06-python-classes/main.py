#!/usr/bin/python3
Square = __import__('101-square').Square

my_square = Square(0, (10, 10))
print(my_square)
my_square = Square(0, (10, 0))
print(my_square)
my_square = Square(0, (0, 0))
print(my_square)