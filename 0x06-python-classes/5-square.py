#!/usr/bin/python3
class Square:
    """ Defines a square by its size
    """
    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
	""" Returns the square
        """
        return (self.__size ** 2)

    def my_print(self):
	""" Returns the size value
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def size(self):
	""" Set the size value of the square object
        """
        return (self.__size)

    @size.setter
    def size(self, value):
	""" Print a # square
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")
