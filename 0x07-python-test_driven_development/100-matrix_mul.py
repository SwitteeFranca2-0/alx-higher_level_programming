#!/usr/bin/python3
"""Mstrix multiplication modeule"""


def matrix_mul(m_a, m_b):
    """This module multiplies matrices
        Args:
            m_a: m_a is a matrix
            m_b: m_b is a matrix
            """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if any(type(n) is not list for n in m_a):
        raise TypeError("m_a must be a list of lists")
    if any(type(n) is not list for n in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    max = len(m_a[0])
    max_2 = len(m_b[0])
    for r in m_a:
        if any(type(n) not in [int, float] for n in r):
            raise TypeError("m_a should contain only integers or floats")
        if len(r) != max:
            raise TypeError("each row of m_a must be of the same size")

    for r in m_b:
        if any(type(n) not in [int, float] for n in r):
            raise TypeError("m_b should contain only integers or floats")
        if len(r) != max_2:
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = []
    new = []
    i = 0
    j = 0
    val = 0
    for r in m_a:
        for i in range(len(m_a)):
            while(j < len(m_b)):
                val += r[j] * m_b[j][i]
                j += 1
            new.append(val)
            j, val = 0, 0
        new_matrix.append(new)
        new = []
    return new_matrix
