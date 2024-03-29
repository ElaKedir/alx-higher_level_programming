#!/usr/bin/python3
""" A class Square that defines a square"""


class Square:
    """ A class Square that defines a square"""

    def __init__(self, size=0):
        """initialize the square class
        Args:
            size (int): the size of the square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size  #: size of the square
