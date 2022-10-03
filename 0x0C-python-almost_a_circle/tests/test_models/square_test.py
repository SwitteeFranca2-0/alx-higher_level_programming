#!/usr/bin/python3
"""This script unit test the Rec class methods"""

import json
import unittest
import sys
from models.rectangle import Rectangle as Rec
from models.base import Base
from models.square import Square as Sq


class TestRecClass(unittest.TestCase):
    """This class unit test the Rec class"""

    def test_create_Square_class(self):
        """This function tests the creation of a Rec obj"""
        rec = Sq(45, 5, 7, 8)
        self.assertNotEqual(rec.id, 0)

    def test_create_Square_set(self):
        """This function sets and confirms the id status of the obj"""
        rec = Sq(45, 7)
        rec.id = 1
        self.assertEqual(rec.id, 1)
        self.assertEqual(rec.x, 7)
        rec.id = 15
        self.assertEqual(rec.id, 15)
        self.assertEqual(rec.size, 45)

    def test_forError_stringArg_x(self):
        """This is testing for necessary errors raises"""
        self.assertRaises(TypeError, Sq, 23, "finally", 8)

    def test_forError_stringArg_size(self):
        """This is testing for necessary errors raises"""
        self.assertRaises(TypeError, Sq, "finally", 7)

    def test_forError_floatArg_x(self):
        """This is testing for necessary errors raises"""
        self.assertRaises(TypeError, Sq, 23, 15.8, 9)

    def test_forError_floatArg_size(self):
        """This is testing for necessary errors raises"""
        self.assertRaises(TypeError, Sq, 0.87, 7)

    def test_forErrors_eqZeroArgSize(self):
        """This is testing for necessary errors raises"""
        self.assertRaises(ValueError, Sq, 0, 3, 0, -4)

    def test_forErrors_ltZeroY(self):
        """This is testing for necessary errors raises"""
        self.assertRaises(ValueError, Sq, 3, 5, -2)
        self.assertRaises(ValueError, Sq, 0, 5, 3)

    def test_forErrors_ltZeroX(self):
        """This is testing for necessary errors raises"""
        self.assertRaises(ValueError, Sq, 4, -1, 4, 0)

    def test_forErrors_ltZerosize(self):
        """This is testing for necessary errors raises"""
        self.assertRaises(ValueError, Sq, -3, 0, 0, -4)

    def test_forErrors_tupleWSize(self):
        """This is testing for necessary errors raises"""
        self.assertRaises(TypeError, Sq, (1, 1), 3)

    def test_forErrors_ListX(self):
        """This is testing for necessary errors raises"""
        self.assertRaises(TypeError, Sq, 3, [])

    def test_forErrors_dictY(self):
        """This is testing for necessary errors raises"""
        self.assertRaises(TypeError, Sq, 3, 3, {}, -4)

    def test_forErrors_dictSize(self):
        """This is testing for necessary errors raises"""
        self.assertRaises(TypeError, Sq, {}, 3, 4, 7)

    def test_Square_setters_getters_size(self):
        """This function tests the setters and getters"""
        rec2 = Sq(4, 5)
        self.assertEqual(rec2.size, 4)
        rec2.x = 10
        self.assertEqual(rec2.x, 10)

    def test_Square_setters_getters_size(self):
        """This function tests the setters and getters"""
        rec2 = Sq(4, 5)
        self.assertEqual(rec2.size, 4)
        rec2.size = 8
        self.assertEqual(rec2.size, 8)

    def test_Square_setters_getters_x(self):
        """This function tests the setters and getters"""
        rec2 = Sq(4, 5)
        rec2.x = 10
        self.assertEqual(rec2.x, 10)

    def test_Square_setters_getters_y(self):
        rec2 = Sq(4, 5, 6)
        """This function tests the setters and getters"""
        rec2.y = 5
        self.assertEqual(rec2.y, 5)
        self.assertNotEqual(rec2.y, 0)

    def test_Square_area(self):
        """his tests the area method"""
        rec3 = Sq(4, 5)
        self.assertEqual(rec3.area(), 16)
        rec3 = Sq(2, 5)
        self.assertEqual(rec3.area(), 4)

    def test_Square_updateArg(self):
        """his test test the update method"""
        rec3 = Sq(4, 5)
        self.assertEqual(rec3.area(), 16)
        rec3.update(4, 5, 7, 8)
        self.assertNotEqual(rec3.area(), 20)
        self.assertEqual(rec3.id, 4)

    def test_Square_updateArgsKwargs(self):
        """his tests the update method using dictionaries"""
        rec3 = Sq(4, 5)
        self.assertEqual(rec3.area(), 16)
        rec3.update(**({'id': 10, 'size': 8, 'x': 5, 'y': 3}))
        self.assertNotEqual(rec3.size, 8)
        self.assertNotEqual(rec3.area(), 16)
        self.assertEqual(rec3.area(), 64)
        self.assertEqual(rec3.x, 5)

    def test_Square_updateArgsKwargs(self):
        """This tests the update method"""
        rec4 = Sq(4, 5)
        rec4.update(5, 6, 7, 8, 9, **({'id': 8, 'size': 10}))
        self.assertEqual(rec4.id, 5)
        self.assertEqual(rec4.size, 6)
        self.assertEqual(rec4.x, 7)

    def test_Square_toDictionary(self):
        """his tesst the to dictonary method"""
        rec5 = Sq(4, 5)
        rec5.id = 1
        dic_read = rec5.to_dictionary()
        self.assertEqual(dic_read, {'id': 1, 'size': 4, 'x': 5, 'y': 0})
        rec5.update(**({'id': 10, 'size': 2}))
        dic_read = rec5.to_dictionary()
        self.assertEqual(dic_read, {'id': 10, 'size': 2, 'x': 5, 'y': 0})
        rec6 = Sq(4, 5, 7, 8)
        Square_l = [rec5, rec6]
        Square_li = [o.to_dictionary() for o in Square_l]
        self.assertEqual(Square_li, [{'id': 10, 'size': 2, 'x': 5,
                                      'y': 0}, {'id': 8, 'size': 4,
                                                'x': 5, 'y': 7}])
