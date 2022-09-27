#!/usr/bin/python3
"""This module contains the 'print pascal' triangle func"""


def pascal_triangle(n):
    """This prints the pascal triangle"""
    tri, ang, count = [[1]], [], 0
    if n <= 0:
        return []
    while count < n - 1:
        a = 0
        for i in tri[count]:
            ang.append(a + i)
            a = i
        ang.append(a)
        tri.append(ang)
        ang = []
        count += 1
    return tri
