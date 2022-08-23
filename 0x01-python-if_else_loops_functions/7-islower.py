#!/usr/bin/python3
"""Identify if or not an alphabet is lower"""

def islower(c):
    if (ord(c) > 96 and ord(c) < 123):
        return True
    else:
        return False
