#!/usr/bin/python3
"""This is a post request"""

import requests
import sys

r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
print(r.text)
