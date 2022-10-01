#!/usr/bin/python3
"""This module contains the scripts"""

import sys

def update_input_dict(dic_val, status_code):
    for code, count in dic_val.items():
        if code not in dic_val:
            dic_val[code] = 1
        else:
            count += 1

input_val = {}
File_size = 0
for i in range(10):
    try:
        input_data = sys.stdin
        Ip_address, other_info = str(input_data).split(" - ")
        info = other_info.split(" ")
        status_code, file_size = info[4], info[5]
        update_input_dict(input_val, status_code)
        File_size += int(file_size)
    except KeyboardInterrupt:
        break

for k, v in input_val.items():
    print(f"File size: {File_size}")
    print(f"{k}: {v}")




