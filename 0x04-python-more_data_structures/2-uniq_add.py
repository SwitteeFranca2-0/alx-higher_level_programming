#!/usr/bin/python3


def uniq_add(my_list=[]):
    new_list, sum = my_list[:], 0
    for num in my_list:
        num1 = num
        new_list.remove(num)
        if num1 not in new_list:
            sum += num1
    return sum
