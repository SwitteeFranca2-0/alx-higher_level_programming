#!/usr/bin/python3
"""This module ahs the 'from json string' function"""
import json


def from_json_string(my_str):
    """This function converts from a json string"""
    return json.loads(my_str)
