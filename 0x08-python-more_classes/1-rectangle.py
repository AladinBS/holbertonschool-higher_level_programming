#!/usr/bin/python3
"""
Define rectangle
"""
class Rectangle:
    """ rectangle """
    def __init__(self, width=0, height=0):
        """
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height
		
    @property
    def width(self):
        """
            width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            value: width
            TypeError: if width is not an integer
            ValueError: if width is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            value: height
            TypeError: if height is not an integer
            ValueError: if height is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
