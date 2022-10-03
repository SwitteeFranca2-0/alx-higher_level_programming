#!/usr/bin/python3
"""his is a unit test file """

import json
import unittest
from models.base import Base


class TestTheBaseClass(unittest.TestCase):
    """Running tests for the Base class"""

    def test_create_base_object(self):
        """Test to create base object"""
        for i in range(10):
            base = Base()
        self.assertEqual(base.id, 10)

    def test_to_json_string(self):
        """est the to json string class method"""
        list_dic = [{'id': 1, 'width': 2}, {'id': 5, 'width': 7}]
        self.assertEqual(Base.to_json_string(list_dic),
                         '[{"id": 1, "width": 2}, {"id": 5, "width": 7}]')

    def test_to_json_stringEmptyDict(self):
        """est the to json string class method"""
        list_dic = [{}, {}]
        self.assertEqual(Base.to_json_string(list_dic), '[{}, {}]')

    def test_to_json_stringListNone(self):
        """est the to json string class method"""
        list_dic = [None]
        self.assertEqual(Base.to_json_string(list_dic), '[null]')

    def test_to_json_stringLstFalseDic(self):
        """est the to json string class method"""
        list_dic = [{'id'}, {'id'}]
        self.assertRaises(TypeError, Base.to_json_string, list_dic)

    def test_to_json_stringEmptyString(self):
        """est the to json string class method"""
        list_dic = []
        self.assertEqual(Base.to_json_string(list_dic), '[]')

    def test_to_json_stringList(self):
        """est the to json string class method"""
        list_dic = [1, 2, 3]
        self.assertEqual(Base.to_json_string(list_dic), '[1, 2, 3]')

    def test_to_json_stringString(self):
        """est the to json string class method"""
        list_dic = "my name is franca"
        self.assertEqual(Base.to_json_string(list_dic),
                         '"my name is franca"')

    def test_to_json_stringInteger(self):
        """est the to json string class method"""
        list_dic = 12
        self.assertEqual(Base.to_json_string(list_dic), '12')

    def test_to_json_stringTuple(self):
        """est the to json string class method"""
        list_dic = (1, 2)
        self.assertEqual(Base.to_json_string(list_dic), '[1, 2]')

    def test_from_json_stringDict(self):
        """This tests the from_json_string static method"""
        string = '[{"id": 1, "width": 2}, {"id": 5, "width": 7}]'
        self.assertEqual(Base.from_json_string(string),
                         [{'id': 1, 'width': 2}, {'id': 5, 'width': 7}])

    def test_from_json_stringNulledList(self):
        """This tests the from_json_string static method"""
        string = '[null]'
        self.assertEqual(Base.from_json_string(string), [None])

    def test_from_json_stringStringList(self):
        """This tests the from_json_string static method"""
        string = '[]'
        self.assertEqual(Base.from_json_string(string), [])

    def test_from_json_stringString(self):
        """This tests the from_json_string static method"""
        string = '"My nme is franca"'
        self.assertEqual(Base.from_json_string(string), "My nme is franca")

    def test_from_json_stringStringNum(self):
        """This tests the from_json_string static method"""
        string = '12'
        self.assertEqual(Base.from_json_string(string), 12)

    def test_fromJsonStringError(self):
        """his tests for errors"""
        string = '[{"id"}, {"id"}]'
        self.assertRaises(json.decoder.JSONDecodeError,
                          Base.from_json_string, string)


if __name__ == '__main__':
    unittest.main()
