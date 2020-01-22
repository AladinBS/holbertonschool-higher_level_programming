#!/usr/bin/python3
""" Define class student """
class Student:
    """ Create student inst """
    def __init__(self, first_name, last_name, age):
        """ Init """
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def to_json(self, attrs=None):
        """ Return description """
        object = self.__dict__.copy()
        if type(attrs) is list:
            for x in attrs:
                if type(x) is not str:
                    return object

            d_list = {}

            for s in range(len(attrs)):
                for satr in object:
                    if attrs[s] == satr:
                        d_list[satr] = object[satr]
            return d_list

        return object
