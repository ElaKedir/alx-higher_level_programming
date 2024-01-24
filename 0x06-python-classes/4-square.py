#!/usr/bin/python3
""" class Square that defines a square"""


class Square:
    """A class Square that defines a square"""
    def __init__(self, size=0):
        """ initializing square

        Args:
            size (int): size of the square.
        """
        self.size = size

    @property
    def size(self):
        """int: private size.

        Returns:
            Private size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value into size, must be int.

        Args:
            value (int): the size of the square.
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value  #: size of the square

    def area(self):
        """a class method that eturns the area

        Returns:
            area.
        """
        return self.__size * self.__size
