#!/usr/bin/python3
"""Mstrix multiplication modeule"""


def matrix_mul(m_a, m_b):
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if type(any(r for r in m_a)) is not list:
        raise TypeError("m_a must be a list of lists")
    if type(any(r for r in m_b)) is not list:
        raise TypeError("m_b muts be a list of lists")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    max = len(m_a[0])
    max_2 = len(m_b[0])
    for r in m_a:
        if type(any(n for n in r)) is not int and type(any(n for n in r)) :
            raise TypeError("m_a should only contain integers or floats")
        if len(r) != max:
            raise TypeError("each row of m_a must be of the same size")
    
    for r in m_b:
        if type(any(n for n in r)) is not int and type(any(n for n in r)):
            raise TypeError("m_b should only contain integers or floats")
        if len(r) != max_2:
            raise TypeError("each row of m_b must be of the same size")