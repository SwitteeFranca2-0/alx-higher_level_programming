#!/usr/bin/python3
"""This returns an error code if an error occurs"""

import requests
import sys

try:
    r = requests.get(sys.argv[1])
    r.raise_for_status()
    print(r.text)
except requests.exceptions.HTTPError as e:
    print("Error code: {}".format(r.status_code))
