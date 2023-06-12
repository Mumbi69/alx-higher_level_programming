#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_value = my_list[0]
    for int in my_list:
        if int > max_value:
            max_value = int

    return max_value
