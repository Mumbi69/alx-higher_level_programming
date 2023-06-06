#!/usr/bin/python3
from decimal import Decimal

def pow(a, b):
    result = Decimal(1)

    if b < 0:
        a = Decimal(1) / Decimal(a)
        b = -b

    for _ in range(b):
        result *= Decimal(a)

    return result
