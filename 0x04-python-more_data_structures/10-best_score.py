#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maximum = None
    max_value = float('-inf')
    for key, value in a_dictionary.items():
        if value > max_value:
            maximum = key
            max_value = value
    return maximum
