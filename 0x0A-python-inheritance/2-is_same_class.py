#!/usr/bin/python3
"""Defines a function class to check exact same object."""


def is_same_class(obj, a_class):
    """Check if object is exactly an instance of a given class"""
    if type(obj) == a_class:
        return True
    return False
