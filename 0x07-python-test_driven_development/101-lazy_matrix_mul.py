#!/usr/bin/python3
"""This module multiplies matrixes"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
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
    if len(m_a) == 0 or all(len(n) == 0 for n in m_a):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or all(len(n) == 0 for n in m_b):
        raise ValueError("m_b can't be empty")

    max = len(m_a[0])
    max_2 = len(m_b[0])
    if any(type(n) not in [int, float] for r in m_a for n in r):
        raise TypeError("m_a should contain only integers or floats")
    if any(len(r) != max for r in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if any(type(n) not in [int, float] for r in m_b for n in r):
        raise TypeError("m_b should contain only integers or floats")
    if any(len(r) != max_2 for r in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    return np.dot(m_a, m_b)
