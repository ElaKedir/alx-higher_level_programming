#!/usr/bin/python3
"""
A module that returns the list of available attributes and methods
of an object.
"""


def lookup(obj):
    """
    the function
    :param obj: the object
    :return: the list of available attributes.
    """
    return dir(obj)
