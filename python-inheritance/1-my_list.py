#!/usr/bin/python3
"""Creating class that inherits from list"""


class MyList(list):
    """list sublclass"""

    def print_sorted(self):
        """Prints a list in ascending order"""
        print(sorted(self))
