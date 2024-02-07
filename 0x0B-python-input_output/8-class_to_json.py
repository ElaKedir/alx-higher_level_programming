#!/usr/bin/python3
""" A module that returns the dictionary description with a simple
data structure for a JSON serialization of an object
"""


def class_to_json(obj):
    """ A function that retuns the dictionary description of an obj """

    result = {}
    if hasattr(obj, "__dict__"):
        result = obj.__dict__.copy()
    return result
