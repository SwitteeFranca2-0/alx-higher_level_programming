#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new_list = []
    for num in my_list:
        num2 = num
        if num == search:
            num2 = replace
        new_list.append(num2)
    return new_list
