#!/usr/bin/python3
def max_integer(my_list=[]):
    max = my_list[0]
    if my_list == "":
        return (None)
    for n in range(len(my_list)):
        if my_list[n] > max:
            max = my_list[n]
    return (max)
