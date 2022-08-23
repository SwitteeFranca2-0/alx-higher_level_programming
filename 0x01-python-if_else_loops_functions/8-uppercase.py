#!/usr/bin/python3
"""Print uppercase"""


def uppercase(str):
    i = 0
    for letter in str:
        if (ord(letter) > 96 and ord(letter) < 123):
            letter = chr(65 + ord(letter) - 97)
        print(letter, end="")
    print("")
