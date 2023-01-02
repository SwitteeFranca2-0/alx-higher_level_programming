#!/usr/bin/python3
"""This script sends a request to a url, displays a particular info"""

import urllib.request
import sys

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        infos = response.info()
        print(infos.get("X-Request-Id"))
