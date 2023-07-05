#!/usr/bin/python3
"""Defines the first and last name"""


def say_my_name(first_name, last_name=""):
    """This function prints My name is <first name> <last name>"""
    if not isinstance(first_name, string):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, string):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
