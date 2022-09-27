#!/usr/bin/python3
"""This module the "save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """Write a JSON presentation of a string into a file"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
