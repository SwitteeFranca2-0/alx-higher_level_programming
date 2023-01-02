#!/usr/bin/python3
"""This is a post request to a url"""

import requests
import sys

payload = {'email': sys.argv[2]}
r = requests.post(sys.argv[1], data=payload)
print(r.text)
