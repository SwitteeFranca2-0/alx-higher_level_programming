#!/usr/bin/python3
"""This script unit test the Rec class methods"""

import json
import unittest
import sys
from models.rectangle import Rectangle as Rec
from models.base import Base


class TestRecClass(unittest.TestCase):
    """This class unit test the Rec class"""

    def test_create_rec_class(self):
        """This function tests the creation of a Rec obj"""
        rec = Rec(45, 7)
        self.assertNotEqual(rec.id, 0)

    def test_create_rec_set(self):
        """This function sets and confirms the id status of the obj"""
        rec = Rec(45, 7)
        rec.id = 1
        self.assertEqual(rec.id, 1)
        self.assertEqual(rec.x, 0)
        rec.id = 15
        self.assertEqual(rec.id, 15)
        self.assertEqual(rec.height, 7)

    def test_forError_stringArg_Height(self):
        """This is testing for necessary errors raises"""
        self.assertRaises(TypeError, Rec, 23, "finally")

    def test_forError_stringArg_Wdith(self):
        """This is testing for necessary errors raises"""
        self.assertRaises(TypeError, Rec, "finally", 7)

    def test_forError_floatArg_Height(self):
        """This is testing for necessary errors raises"""
        self.assertRaises(TypeError, Rec, 23, 15.8)

    def test_forError_floatArg_Wdith(self):
        """This is testing for necessary errors raises"""
        self.assertRaises(TypeError, Rec, 0.87, 7)

    def test_forErrors_eqZeroArgWidth(self):
        """This is testing for necessary errors raises"""
        self.assertRaises(ValueError, Rec, 0, 3, 0, -4)

    def test_forErrors_ltZeroWdith(self):
        """This is testing for necessary errors raises"""
        self.assertRaises(ValueError, Rec, 3, -2)
        self.assertRaises(ValueError, Rec, 0, 3)

    def test_forErrors_ltZeroX(self):
        """This is testing for necessary errors raises"""
        self.assertRaises(ValueError, Rec, 4, 4, -1, 0)

    def test_forErrors_ltZeroHeight(self):
        """This is testing for necessary errors raises"""
        self.assertRaises(ValueError, Rec, 3, 0, 0, -4)

    def test_forErrors_tupleWidth(self):
        """This is testing for necessary errors raises"""
        self.assertRaises(TypeError, Rec, (1, 1), 3)

    def test_forErrors_ListHeight(self):
        """This is testing for necessary errors raises"""
        self.assertRaises(TypeError, Rec, 3, [])

    def test_forErrors_dictX(self):
        """This is testing for necessary errors raises"""
        self.assertRaises(TypeError, Rec, 3, 3, {}, -4)

    def test_forErrors_dictY(self):
        """This is testing for necessary errors raises"""
        self.assertRaises(TypeError, Rec, 3, 3, 4, {})

    def test_Rec_setters_getters_wiidth(self):
        """This function tests the setters and getters"""
        rec2 = Rec(4, 5)
        self.assertEqual(rec2.width, 4)
        rec2.width = 10
        self.assertEqual(rec2.width, 10)

    def test_Rec_setters_getters_height(self):
        """This function tests the setters and getters"""
        rec2 = Rec(4, 5)
        self.assertEqual(rec2.height, 5)
        rec2.height = 8
        self.assertEqual(rec2.height, 8)

    def test_Rec_setters_getters_x(self):
        """This function tests the setters and getters"""
        rec2 = Rec(4, 5)
        rec2.x = 5
        self.assertEqual(rec2.x, 5)

    def test_Rec_setters_getters_y(self):
        rec2 = Rec(4, 5)
        """This function tests the setters and getters"""
        rec2.y = 5
        self.assertEqual(rec2.y, 5)
        self.assertNotEqual(rec2.y, 0)

    def test_Rec_area(self):
        """his tests the area method"""
        rec3 = Rec(4, 5)
        self.assertEqual(rec3.area(), 20)
        rec3 = Rec(2, 5)
        self.assertEqual(rec3.area(), 10)

    def test_rec_updateArg(self):
        """his test test the update method"""
        rec3 = Rec(4, 5)
        self.assertEqual(rec3.area(), 20)
        rec3.update(4, 5, 7, 8, 0)
        self.assertNotEqual(rec3.area(), 20)
        self.assertEqual(rec3.id, 4)

    def test_rec_updateArgsKwargs(self):
        """his tests the update method using dictionaries"""
        rec3 = Rec(4, 5)
        self.assertEqual(rec3.area(), 20)
        rec3.update(**({'width': 10, 'height': 4, 'x': 5, 'y': 3}))
        self.assertNotEqual(rec3.width, 4)
        self.assertNotEqual(rec3.area(), 20)
        self.assertEqual(rec3.area(), 40)
        self.assertEqual(rec3.x, 5)

    def test_Rec_updateArgsKwargs(self):
        """This tests the update method"""
        rec4 = Rec(4, 5)
        rec4.update(5, 6, 7, 8, 9, **({'id': 8, 'height': 10}))
        self.assertEqual(rec4.id, 5)
        self.assertEqual(rec4.width, 6)
        self.assertEqual(rec4.x, 8)

    def test_Rec_toDictionary(self):
        """his tesst the to dictonary method"""
        rec5 = Rec(4, 5)
        rec5.id = 1
        d = rec5.to_dictionary()
        self.assertEqual(d, {'id': 1, 'width': 4, 'height': 5, 'x': 0, 'y': 0})
        rec5.update(**({'id': 10, 'width': 2}))
        d = rec5.to_dictionary()
        self.assertEqual(d, {'id': 10, 'width': 2, 'height': 5,
                             'x': 0, 'y': 0})
        rec6 = Rec(4, 5, 7, 8, 9)
        rec_l = [rec5, rec6]
        rec_li = [o.to_dictionary() for o in rec_l]
        self.assertEqual(rec_li, [{'id': 10, 'width': 2, 'height': 5,
                                  'x': 0, 'y': 0},
                                  {'id': 9, 'width': 4, 'height': 5,
                                  'x': 7, 'y': 8}])
