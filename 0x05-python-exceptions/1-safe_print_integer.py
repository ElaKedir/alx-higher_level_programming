#!/usr/bin/python3

def safe_print_integer(value):
    """ A function that prints an integer with "{:d}".format().

    Args:
        value (int): The integer.

    Returns:
        True if the value is an integer, Otherwise, returns False.
    """

    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
