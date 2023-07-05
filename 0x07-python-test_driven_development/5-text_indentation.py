#!/usr/bin/python3
"""Defines text indentation of the function."""


def text_indentation(text):
    """This function prints a text with 2 new lines after each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    m = 0
    while m < len(text) and text[m] == ' ':
        m += 1

    while m < len(text):
        print(text[m], end="")
        if text[m] == "\n" or text[m] in ".?:":
            if text[m] in ".?:":
                print("\n")
            m += 1
            while m < len(text) and text[m] == ' ':
                m += 1
            continue
        m += 1
