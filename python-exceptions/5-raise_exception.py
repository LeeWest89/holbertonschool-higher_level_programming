#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
        print("{}".format, (result))
        if result == 0:
            return (None)
    except:
