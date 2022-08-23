#!/usr/bin/python3
"""remove character at indicated location"""

def remove_char_at(str, n):
    str1 = ""
    i = 0
    for letter in str:
        if (i != n):
            str1 += letter
        i += 1
    return str1
