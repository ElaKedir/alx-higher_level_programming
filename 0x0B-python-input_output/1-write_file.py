#!/usr/bin/python3
""" A module that contains a function that writes to a text file
"""


def write_file(filename="", text=""):
    """ A function that writes to a text file

    Args:
        filename: filename
        text: text to write

    Raises
        Exception: when the file can be opened

    """

    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
