#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    roman = 0
    prev_value = 0

    process_char = lambda char: roman + roman_values[char] if roman_values[char] >= prev_value else roman - roman_values[char]

    for char in reversed(roman_string):
        roman = process_char(char)
        prev_value = roman_values[char]

    return roman
