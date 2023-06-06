#!/usr/bin/python3
def uppercase(string):
    result = ""
    for c in string:
        if 'a' <= c <= 'z':
            result += chr(ord(c) - 32)
        else:
            result += c
    print("{:s}".format(result))
    print()
