#!/usr/bin/python3
"""Defines a square."""


def print_square(size):
    """This function prints a square with the character #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for m in range(size):
        [print("#", end="") for s in range(size)]
        print("")
