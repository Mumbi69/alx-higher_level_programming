#!/usr/bin/python3
def uppercase(string):
    result = ""
    for c in string:
        if 'a' <= c <= 'z':
            result += chr(ord(c) - ord('a') + ord('A'))
        else:
            result += c
    print("{:s}".format(result))
