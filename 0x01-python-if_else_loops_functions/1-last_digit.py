#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
abs = number * -1
if (number > 0):
    if (number % 10 == 0):
        print(f"Last digit of {number} is 0 and is 0")
    elif (number % 10 > 5):
        print(f"Last digit of {number} is {number % 10} and is greater than 5")
    else:
        print(f"Last digit of {number} is {number % 10} and is lesser than "
            + "6 and not 0")
else:
    print(f"Last digit of {number} is -{(number * -1) % 10} and is lesser than"
        + " 6 and not 0")
