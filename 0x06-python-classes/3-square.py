#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size has to be an integer")
        elif size < 0:
            raise ValueError("size has to be >= 0")
        else:
            self.__size = size

    def area(self):
        return (self.__size ** 2)
