#!/usr/bin/python3
"""
A module  that adds two numbers
"""


def add_integer(a, b=98):
    """ A function that adds two integers and/or float numbers

    Args:
        a: first number
        b: second number

    Returns:
        The addition of the two numbers

    Raises:
        TypeError: If a or b aren't integer and/or float numbers

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
