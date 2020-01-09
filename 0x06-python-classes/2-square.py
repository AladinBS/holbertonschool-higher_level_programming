#!/usr/bin/python3
class Square:
    """ This class defines a square"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("has to be an integer")
        elif size < 0:
            raise ValueError("size has to be >= 0")
        else:
            self.__size = int(size)
