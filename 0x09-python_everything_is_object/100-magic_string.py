#!/usr/bin/python3
def magic_string():
    num = getattr(magic_string, 'n', 0) + 1
    return ("Best School, " * (num - 1) + "Best School")

for i in range(10):
    print(magic_string())