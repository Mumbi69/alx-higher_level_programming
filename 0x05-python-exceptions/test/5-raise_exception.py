#!/usr/bin/python3
def raise_exception():
    try:
        raise NameError()
    except NameError:
        print("")
        raise
