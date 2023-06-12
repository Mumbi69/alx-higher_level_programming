#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, int in enumerate(row):
            if i != len(row) - 1:
                print("{:d} ".format(int), end='')
            else:
                print("{:d}".format(int), end='')
        print()
