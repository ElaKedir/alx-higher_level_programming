#!/usr/bin/python3
"""

A module composed of functions that prints a square with the character #

"""


def print_square(size):
    """ A function that prints a square with the character #

    Args:
        size: size of the square printed

    Returns:
        Nothing

    Raises:
        TypeError: If size is not an integer number


    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
