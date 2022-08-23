#!/usr/bin/python3
for num in range(0, 100):
    if (num == 99):
        print(num, end="\n")
    else:
        print(f"{num:02}", end=", ")
