#!/usr/bin/python3
def uppercase(string):
    for c in string:
        if 'a' <= c <= 'z':
            print("{:c}".format(ord(c) - 32), end="")
        else:
            print("{:c}".format(ord(c)), end="")
    print()
