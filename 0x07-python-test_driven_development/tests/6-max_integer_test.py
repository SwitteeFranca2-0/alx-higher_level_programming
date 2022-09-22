#!/usr/bin/python3
"""Module checks for max iinteger"""

import unittest

max = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This class tests the imported function"""

    def test_max_end_no_list(self):
        """This function fiinds the maximum of a group of numbers"""
        no_list = [1, 2, 3, 4, 5]
        self.assertEqual(max(no_list), 5)

    def test_max_beginning_no_list(self):
        """This function fiinds the maximum of a group of numbers"""
        no_list = [9, 3, 5, 6, 7]
        self.assertEqual(max(no_list), 9)

    def test_max_middle_no_list(self):
        """This function fiinds the maximum of a group of numbers"""
        no_list = [3, 4, 5, 8, 5, 2, 1]
        self.assertEqual(max(no_list), 8)

    def test_signed_num_list(self):
        """This function fiinds the maximum of a group of numbers"""
        no_list = [3, -5, 6, 7, 8]
        self.assertEqual(max(no_list), 8)

    def test_all_signed_num(self):
        """This function fiinds the maximum of a group of numbers"""
        no_list = [-5, -8, -10, -2]
        self.assertEqual(max(no_list), -2)

    def test_num(self):
        """This function fiinds the maximum of a group of numbers"""
        no_list = [1]
        self.assertEqual(max(no_list), 1)

    def test_empty_list(self):
        """This function fiinds the maximum of a group of numbers"""
        self.assertEqual(max(), None)


if __name__ == '__main__':
    unittest.main()
