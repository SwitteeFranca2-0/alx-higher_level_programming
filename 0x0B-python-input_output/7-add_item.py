#!/usr/bin/python3
"""This module contains the a script"""
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


js_list = [i for i in argv if argv.index(i) != 0]
save_to_json_file(js_list, "add_item.json")
