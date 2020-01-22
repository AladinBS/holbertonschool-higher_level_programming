#!/usr/bin/python3
""" Define class student """
class Student:
    """ Student inst """
    def __init__(self, first_name, last_name, age):
        """ Init """
        self.last_name = last_name
        self.age = age
        self.first_name = first_name

    def to_json(self):
        """ Dir discrp """
        return self.__dict__.copy()
