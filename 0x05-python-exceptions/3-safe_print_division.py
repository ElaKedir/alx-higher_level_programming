#!/usr/bin/python3

def safe_print_division(a, b):
    """ A function that divides 2 integers and prints the result.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        The value of the division, otherwise: None.
    """
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
