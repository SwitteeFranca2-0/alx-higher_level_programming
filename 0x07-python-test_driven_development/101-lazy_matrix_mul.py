#!/usr/bin/python3
"""This module multiplies matrixes"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """This module multiplies matrices
        Args:
            m_a: m_a is a matrix
            m_b: m_b is a matrix
    """
    return np.dot(m_a, m_b)
