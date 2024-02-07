#!/usr/bin/python3
""" A module that executes a function that appends a line """


def append_after(filename="", search_string="", new_string=""):
    """ A function that appends a new line when a string is found

    Args:
        filename: filename
        search_string: string to search
        new_string: string to append

    """

    rs_line = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            rs_line += [line]
            if line.find(search_string) != -1:
                rs_line += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(rs_line))
