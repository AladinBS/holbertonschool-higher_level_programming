#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size has to be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size has to be an integer")

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size has to be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size has to be an integer")
