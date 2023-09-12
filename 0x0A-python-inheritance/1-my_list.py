#!/usr/bin/python3
"""
 class MyList that inherits from list
"""


class MyList(list):
    """
    A Class that sort a list in ascending order
    """
    def print_sorted(self):
        """
        A function that sort a list in ascending order
        """
        sorted_list = sorted(self)
        print(sorted_list)
