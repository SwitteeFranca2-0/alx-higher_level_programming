#!/usr/bin/python3

"""Print all letters apart from q and e"""

for i in range(97, 123):
    if (chr(i) == 'q' or chr(i) == 'e'):
        continue
    print(f"{chr(i)}", end="")
