#!/usr/bin/python3


def roman_to_int(roman_string):
    i = 0
    num = 0
    r_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if not roman_string or type(roman_string) != str:
        return 0
    r = roman_string
    while(i < len(r)):
        if i + 1 == len(r):
            num += r_num.get(r[i])
        if i + 1 < len(r):
            if r_num.get(r[i]) > r_num.get(r[i + 1]):
                num += r_num[r[i]]
            elif r_num.get(r[i]) < r_num.get(r[i + 1]):
                num -= r_num[r[i]]
            else:
                if i+2 < len(r) and r_num.get(r[i + 2]) > r_num.get(r[i]):
                    num -= r_num[r[i]] + r_num[r[i+1]]
                    i += 1
                else:
                    num += r_num[r[i]] + r_num[r[i+1]]
                    i += 1
        i += 1
    return num
