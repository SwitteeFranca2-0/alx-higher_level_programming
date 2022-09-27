#!/usr/bin/python3
"""This module contains the a script"""
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

js_list = []

try:
    js_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    [js_list.append(i) for i in argv if argv.index(i) != 0]
save_to_json_file(js_list, "add_item.json")
