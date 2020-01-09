#!/usr/bin/python3
class Square:
	""" It defines a square by its size"""
    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size has to be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size has to be an integer")
