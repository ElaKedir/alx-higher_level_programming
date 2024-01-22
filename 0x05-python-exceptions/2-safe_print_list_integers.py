#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """ A function that prints the first x elements
    of a list and only integers.

    Args:
        my_list (list): The list.
        x (int): The integer.

    Returns:
        The real number of integers printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            pass
        else:
            count += 1
    print("")
    return (count)
