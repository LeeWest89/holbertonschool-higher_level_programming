#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_key = sorted(a_dictionary.items())
    for key, value in sorted_key:
        print(f'{key}: {value}')
