#!/usr/bin/python3

"""This python script sens a request to alx url"""

import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        the_response = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(the_response)))
        print('\t- content: {}'.format(the_response))
        print('\t- utf8 content: {}'.format(the_response.decode("utf-8")))
