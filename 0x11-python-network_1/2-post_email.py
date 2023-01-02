#!/usr/bin/python3
"""this posts email to a url"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    url_values = urllib.parse.urlencode(data)
    url_values = url_values.encode('utf-8')
    req = urllib.request.Request(sys.argv[1], url_values)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
