#!/usr/bin/python3


def weight_average(my_list=[]):
    average = 0
    num = 0
    if len(my_list) == 0:
        return 0
    for tup in my_list:
        average += tup[0] * tup[1]
        num += tup[1]
    return average / num
