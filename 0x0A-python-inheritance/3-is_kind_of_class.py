#!/usr/bin/python3
"""Defines a same class or inherit from."""


def is_kind_of_class(obj, a_class):
    """Check if object is an instance or inherited instance."""
    if isinstance(obj, a_class):
        return True
    return False
