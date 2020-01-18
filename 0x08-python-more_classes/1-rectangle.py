#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        """
	width: width of rec
	height: height of rec
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
	width rec
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
	value: width
        TypeError: in case not an int
        ValueError: in case width is negative
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        height of rec
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        value: h
        TypeError: in case not an int
        ValueError: in case width is negative
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
