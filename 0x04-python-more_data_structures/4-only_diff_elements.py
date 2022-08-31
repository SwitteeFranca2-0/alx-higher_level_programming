#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    set_e = [el for el in set_1 if el not in set_2]
    return set_e + [el for el in set_2 if el not in set_1]
