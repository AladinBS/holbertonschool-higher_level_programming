#!/usr/bin/python3
class Square:
    """Square defined"""
    def __init__(self, size=0):
        """This is a method"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Another method"""
        return (self.__size ** 2)

    @property
    def size(self):
        """Returns size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Value of square object"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
