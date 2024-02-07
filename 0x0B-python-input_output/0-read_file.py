#!/usr/bin/python3
""" A module that contains a function that reads from a file """


def read_file(filename=""):
    """ A function that reads from a file

    Args:
        filename: filename

    Raises
        Exception: when the file can be opened

    """

    with open(filename, 'r', encoding="utf-8") as file:
        read_data = file.read()
        print(read_data, end='')
