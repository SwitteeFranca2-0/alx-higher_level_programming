#!/usr/bin/python3
"""This script displays an info"""

import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers['X-Request-Id'])
