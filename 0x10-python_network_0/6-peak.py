#!/usr/bin/python3

def find_peak(list_of_integers):
    if len(list_of_integers):
        new_list = sorted(list_of_integers)
        peak = new_list[-1]
        return peak
