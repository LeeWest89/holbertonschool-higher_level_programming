#!/usr/bin/python3
"""Creating class that inherits from list"""


class MyList(list):

    def print_sorted(self):
        """Prints a list in ascending order"""
        sort_list = sorted(self)
        print(sort_list)
