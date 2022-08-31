#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    a = a_dictionary
    if len(a_dictionary) != 0:
        list_1 = [keys for keys in a if a.get(keys) == value]
        for key in list_1:
            if key in a_dictionary:
                del a_dictionary[key]
    return a_dictionary
