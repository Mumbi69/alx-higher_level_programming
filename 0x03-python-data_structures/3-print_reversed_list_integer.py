#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reversed_list = []
    for int in reversed(my_list):
        print("{:d}".format(int))
