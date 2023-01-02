#!/usr/bin/python3
"""This prints all commmits in a particular repositoy"""

import sys
import requests

if __name__ == "__main__":
    e = sys.argv[1]
    o = sys.argv[2]
    r = requests.get('https://api.github.com/repos/{}/{}/commits'.format(o, e))
    r = r.json()
    try:
        for i in range(10):
            sha = r[i].get('sha')
            author = r[i].get('commit').get('author').get('name')
            print('{}: {}'.format(sha, author))
    except IndexError:
        pass
