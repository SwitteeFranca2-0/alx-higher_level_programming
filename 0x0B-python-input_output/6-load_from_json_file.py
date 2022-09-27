#!/usr/bin/python3
"""his module contains the "load from jason file" module """
import json


def load_from_json_file(filename):
    """This function creates object from a json file"""
    with open(filename, 'r') as f:
        return json.loads(f.read())
