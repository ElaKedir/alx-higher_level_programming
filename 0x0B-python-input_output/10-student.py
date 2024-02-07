#!/usr/bin/python3
""" A module that defines the class Student
"""


class Student:
    """ Class to create student instances """

    def __init__(self, first_name, last_name, age):
        """ A majic method to initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ A method that returns directory description """
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj

            dir_list = {}

            for iatr in range(len(attrs)):
                for satr in obj:
                    if attrs[iatr] == satr:
                        dir_list[satr] = obj[satr]
            return dir_list

        return obj
