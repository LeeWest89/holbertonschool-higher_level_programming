#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return (0)
    roman_numerals = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    number = 0
    prev = 0
    for i in roman_string:
        for key, value in roman_numerals.items():
            if i == key:
                if prev == 0 or prev >= value:
                    number += value
                elif prev < value:
                    number += value - (2 * prev)
                prev = value
    return (number)
