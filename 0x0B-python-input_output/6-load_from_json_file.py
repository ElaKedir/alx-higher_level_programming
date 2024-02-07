#!/usr/bin/python3
""" A module that creates an Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """ A function that creates an Object from a JSON file

    Args:
        filename: textfile name

    Raises:
        Exception: when the object can't be encoded

    """
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
