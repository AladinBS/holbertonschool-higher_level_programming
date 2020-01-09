#!/usr/bin/python3
class Square:
    """ This class defines a square"""
    def __init__(self, x=0):
        if not isinstance(x, int):
            raise TypeError("x has to be an integer")
        elif x < 0:
            raise ValueError("x has to be >= 0")
        else:
            self.__x = int(x)
