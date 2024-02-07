#!/usr/bin/python3
"""
A module that holds a 'class' MyList that inherits from 'list'.
"""


class MyList(list):
    """A class that inherits from list"""
    def print_sorted(self):
        """A method that prints a sorted list in ascending order."""
        print(sorted(self))
