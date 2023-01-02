#!/usr/bin/python3
"""This scripts finds api"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""
    load = {'q': letter}
    r = requests.post('http://0.0.0.0:5000/search_user', params=load)
    try:
        dic = r.json()
        if dic == {}:
            print("No result")
        else:
            print("[{}] {}".format(dic.get("id"), dic.get("name")))
    except ValueError:
        print("Not a valid JSON")
