#!/usr/bin/python3
import math


class MagicClass:

    """ find the perim """
    def circumference(self):
        return (2 * math.pi * self.__radius)

    """ Find the area"""
    def area(self):
        return ((self.__radius ** 2) * math.pi)

    """A class to save info"""
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius
