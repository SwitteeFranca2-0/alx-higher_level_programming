#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in row:
            if(row.index(num) == len(row) - 1 and len(row) != 0):
                print("{:d}".format(num), end="")
                continue
            print("{:d}".format(num), end=" ")
        print("")
