#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """A function that Print x elememts of a list.

    Args:
        my_list (list): The list.
        x (int): The number of elements to be printed.

    Returns:
        The number of elements printed.
    """
    r = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            r += 1
        except IndexError:
            break
    print("")
    return (r)
