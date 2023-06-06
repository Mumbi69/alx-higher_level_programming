#!/usr/bin/python3
from itertools import combinations

for combo in combinations(range(10), 2):
    print("{:02d}".format(combo[0] * 10 + combo[1]), end=", ")
print("\n")
