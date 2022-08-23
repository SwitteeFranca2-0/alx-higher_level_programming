#!/usr/bin/python3

for num in range(0, 9):
    for num2 in range(num + 1, 10):
        if (num == 8 and num2 == 9):
            print(f"89", end="\n")
        else:
            print(f"{num}{num2}", end=", ")
