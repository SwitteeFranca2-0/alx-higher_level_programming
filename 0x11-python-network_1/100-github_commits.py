#!/usr/bin/python3
"""This prints all commmits in a particular repositoy"""

import sys
import requests

if __name__ == "__main__":
    e = sys.argv[1]
    o = sys.argv[2]
    r = requests.get('https://api.github.com/repos/{}/{}/commits'.format(e, o))
    dic = r.json()
    for i in dic:
        sha = i.get('sha')
        author = i.get('commit').get('author').get('name')
        print('{}: {}'.format(sha, author))
