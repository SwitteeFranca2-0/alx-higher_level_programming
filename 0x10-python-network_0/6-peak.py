#!/usr/bin/python3
"""Finding the mximum of a list of numbers """


def find_peak(list_of_integers):
    """Finding th e,aximum of a list of integers"""
    if len(list_of_integers):
        new_list = sorted(list_of_integers)
        peak = new_list[-1]
        return peak
