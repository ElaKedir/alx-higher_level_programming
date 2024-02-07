#!/usr/bin/python3
"""
A module that holds the function that returns True if the object is exactly
an instance of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """
    A function that returns
    :param obj: the object
    :param a_class: the class
    :return: True if the object is exactly an instance otherwise returns false
    """
    return True if type(obj) is a_class else False
