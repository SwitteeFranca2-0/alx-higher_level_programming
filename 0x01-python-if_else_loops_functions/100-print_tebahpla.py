#!/usr/bin/python3
"""Print alternating cases of the alphabet in reverse"""

for num in range(122, 96, -1):
    if (num % 2):
        num = 65 + num - 97
    print("{}".format(chr(num)), end="")
